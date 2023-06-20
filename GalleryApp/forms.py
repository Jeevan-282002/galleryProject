from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django import forms
from . models import ImageModel

class LoginForm(AuthenticationForm):

    username = forms.CharField(label='Enter Your Username' , widget=forms.TextInput(attrs={'class':'form-control'}))

    password = forms.CharField(label='Enter Your Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User


class RegisterForm(UserCreationForm):

    password1 = forms.CharField(label='Enter Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2 = forms.CharField(label='Confirm Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


        labels = {
            'username':'Enter Username' , 'first_name' : 'Enter first Name' , 'last_name':'Enter Last Name','email':'Enter Email-ID'

        }

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['img_title','image','category']


        labels = {
            'img_title' : 'Enter Image Title',
            'image' : 'Upload Image',
            'category' : 'Select Image Category'
        }


        widgets = {
            'img_title' : forms.TextInput(attrs={'class':'form-control'}),
            'image' : forms.FileInput(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'}),

        }  