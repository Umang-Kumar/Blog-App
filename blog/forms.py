from django import forms
from .models import ContactProfile


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

class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'message', 'subject')