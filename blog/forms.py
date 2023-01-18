from django import forms
from .models import ContactProfile, Post


class ContactForm(forms.ModelForm):
	class Meta:
		model = ContactProfile
		fields = [
			'name',
			'email',
			'message',
			'subject',
		]
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.TextInput(attrs={'class': 'form-control'}),
			'message': forms.Textarea(attrs={'class': 'form-control'}),
			'subject': forms.TextInput(attrs={'class': 'form-control'}),
		}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
			'title', 
			'category',
			'body', 
			'image',
		]
        widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'category': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'image': forms.FileInput(attrs={'class': 'form-control'}),
		}