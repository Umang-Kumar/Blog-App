from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User


from . forms import ContactForm, PostForm

# Create your views here.
from django.contrib import messages
from .models import (
		UserProfile,
        Post,
)

class IndexView(generic.TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		posts = Post.objects.all()
		context['posts'] = posts
		
		return context
    

class PostView(generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post.html'


class AboutView(generic.TemplateView):
	template_name = "about.html"


class PostBlog(generic.FormView):
	template_name = "postBlog.html"
	form_class = PostForm
	# fields = ['title', 'content', 'image', 'is_active']
	success_url = "/"

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class ContactView(generic.FormView):
	template_name = "contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)

def login(request):
	if request.user.is_authenticated:
		return redirect('blog:index')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			auth_login(request, user)
			# messages.success(request, 'Login Successful')
			return redirect('blog:index')
		else:
			messages.error(request, 'Invalid Username or Password')
			return render(request, 'registration/login.html')
	return render(request, 'login.html')


def signup(request):
	if request.user.is_authenticated:
		return redirect('blog:index')
	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['cpassword']	

		if password != cpassword:
			messages.error(request, 'Confirm Password does not match')
			return render(request, 'registration/signup.html')	
		else:
			if User.objects.filter(username=username).exists():
				messages.error(request, 'Username already exists')
				return render(request, 'registration/signup.html')
			else:
				if User.objects.filter(email=email).exists():
					messages.error(request, 'Email already exists')
					return render(request, 'registration/signup.html')
				else:
					user = User.objects.create_user(username=username, email=email, password=password, first_name=fname, last_name=lname)
					user.save()
					messages.success(request, 'Account created successfully')
					return render(request, 'registration/signup.html')	
	return render(request, 'registration/signup.html')


def logout(request):
	auth_logout(request)
	return render('blog:index')