#forms module provides many types of input fields for us to use 
from django import forms
#Django has a pregenerated Model named User that can be added to
from django.contrib.auth.models import User
#Django has a pregenerated Form that can be inherited from and added to
from django.contrib.auth.forms import UserCreationForm
# I import a model Profile from my models file
from .models import Profile, Quotes
#I import a model Quotes from my models file


#I make my own defined class called UserRegisterForm and it inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
    
    #here you can add more fields to your class
    email = forms.EmailField()
    
    #class Meta specifies the model this form is connected to and the fields
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'            
            ]

#I make my own defined class called UserUpdateForm and it inherits from the forms module
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = [
            'username',
            'email'
            ]

#I make my own defined class called ProfileUpdateForm and it inherits from the forms module
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image',
            ]
        
class QuoteInsertForm(forms.ModelForm):
    class Meta:
        model = Quotes
        fields = [
            'quote',
            'author'
        ]