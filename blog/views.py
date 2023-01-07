from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


from . forms import ContactForm

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


class ContactView(generic.FormView):
	template_name = "contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)