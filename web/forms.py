from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact
from django.forms import widgets
from django.forms.widgets import (EmailInput, TextInput)
                                  





class SignUpForm(UserCreationForm):
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'username'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    password1 = forms.CharField(label="", max_length=80, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password1'}))
    password2 = forms.CharField(label="", max_length=80, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password2'}))
	
	
class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

def __init__(self, *args, **kwargs):
	    super(SignUpForm, self).__init__(*args, **kwargs)


from django import forms

class ContactForm(forms.ModelForm):
    SUBJECT_CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    ]

    choice = forms.ChoiceField(choices=SUBJECT_CHOICES, widget=forms.Select(attrs={"class": "form-control", "placeholder": "Your choice"}))

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject',"choice","phone")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your email'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your subject'})
        self.fields['choice'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your choice'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your phone'})
