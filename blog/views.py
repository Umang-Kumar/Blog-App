from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from . forms import *
from django.contrib import messages
from .models import *


# Create your views here.

# Blog(View, Search, Post)
class IndexView(generic.TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		posts = Post.objects.all()
		latest  = Post.objects.all().order_by('-id')[:3]
		context['posts'] = posts
		context['latest'] = latest
		
		return context
    

class PostView(generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


# Detailed Post and Comments
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post.html'
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(blog=self.get_object())
        print(len(comments))
        context['comments'] = comments
        return context
	
    def post(self, request, *args, **kwargs):
        comment = Comment()
        comment.blog = self.get_object()
        comment.user = request.user
        comment.content = request.POST['content']
        comment.save()
        messages.success(request, "Comment added successfully")
        return self.get(request, *args, **kwargs)

class AboutView(generic.TemplateView):
	template_name = "about.html"


class PostBlog(generic.FormView):
	template_name = "postBlog.html"
	form_class = PostForm
	success_url = "/"

	def form_valid(self, form):
		blogpost = form.save(commit=False)
		blogpost.author = self.request.user
		blogpost.save()
		messages.success(self.request, "Blog post created successfully")
		return super().form_valid(form)


class SearchBlog(generic.View):
    template_name = 'search.html'
    # success_url = '/'

    def post(self, request):
        searched = request.POST['searched']
        blogs = Post.objects.filter(title__contains=searched) | Post.objects.filter(category__contains=searched)
        return render(request, self.template_name, {'searched':searched, 'blogs':blogs})
    def get(self, request):
        return render(request, self.template_name)


# User's Dashboard
class DashboardView(generic.TemplateView):
	template_name = "profile.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		users = UserProfile.objects.filter(is_active=True)
		posts = Post.objects.filter(author=self.request.user)
		context['posts'] = posts
		context['users'] = users
		
		return context


# Edit Profile
class EditProfileView(generic.UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'editProfile.html'
    success_url = "/profile/"

    def get_object(self, queryset=None):
        return self.request.user.userprofile

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully')
        return super().form_valid(form)

# Contact
class ContactView(generic.FormView):
	template_name = "contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)


# Authentication & Registration
class LoginView(generic.View):
    template_name = 'registration/login.html'
    success_url = "/"
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:index')
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('blog:index')
        else:
            messages.error(request, 'Invalid Username or Password')
            return render(request, self.template_name)


class SignupView(generic.View):
    template_name = 'registration/signup.html'
    success_url = "/"
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:index')
        return render(request, self.template_name)

    def post(self, request):
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password != cpassword:
            messages.error(request, 'Confirm Password does not match')
            return render(request, self.template_name)
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return render(request, self.template_name)
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return render(request, self.template_name)
                else:
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=fname, last_name=lname)
                    user.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('blog:index')


class LogoutView(generic.View):

    def get(self, request):
        auth_logout(request)
        return redirect('blog:index')