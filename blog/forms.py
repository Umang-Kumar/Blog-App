from django import forms
from .models import *


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
			'title': forms.TextInput(attrs={'class': 'form-control', 'required': 'True'}),
			'category': forms.TextInput(attrs={'class': 'form-control' , 'required': 'True'}),
			'body': forms.Textarea(attrs={'class': 'form-control' , 'required': 'True'}),
			'image': forms.FileInput(attrs={'class': 'form-control'}),
		}

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = [
			'avatar',
			'bio',
			'phone_no',
			'facebook',
			'instagram',
			'linkedin',
		]
		widgets = {
			'avatar': forms.FileInput(attrs={'class': 'form-control'}),
			'bio': forms.Textarea(attrs={'class': 'form-control'}),
			'phone_no': forms.TextInput(attrs={'class': 'form-control'}),
			'facebook': forms.TextInput(attrs={'class': 'form-control'}),
			'instagram': forms.TextInput(attrs={'class': 'form-control'}),
			'linkedin': forms.TextInput(attrs={'class': 'form-control'}),
		}