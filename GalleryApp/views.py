import re
from django.shortcuts import render , redirect
# from django.contrib.auth.forms import AuthenticationForm , UserCreationForm

from . forms import LoginForm , RegisterForm , ImageForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

from . models import CategoryModel , ImageModel 
# Create your views here.

def home_view(request):

    if request.user.is_authenticated:
        return redirect('gallery')


    forms = LoginForm()
    context = {'forms':forms}
    return render(request , 'GalleryApp/home.html' , context)


def gallery_view(request):
    Categories = CategoryModel.objects.all()
    Image = ImageModel.objects.all()
    context = {'Categories':Categories , 'Image':Image}
    return render(request,'GalleryApp/gallery.html' , context)


def catimage_view(request, id):
    print('id is' , id)
    Categories = CategoryModel.objects.all()

    cat = CategoryModel.objects.get(id=id)
    Image = ImageModel.objects.filter(category=cat)

    context = {'Categories':Categories ,'Image':Image }
    return render(request,'GalleryApp/gallery.html' , context)


def signup_view(request):
    forms = RegisterForm()

    if request.method == 'POST':
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request , 'User Successfully Register')
            return redirect('home')

    context = {'forms':forms}
    return render(request , 'GalleryApp/signup.html' , context)

def signin_view(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        pass1 = request.POST['password']

        user = authenticate(username = username1 , password = pass1)

        if user is not None:
            login(request,user)
            messages.success(request , 'Successfully user login')
            return redirect('gallery')

            # return redirect('gallery')

        else:
            messages.warning(request , 'Something went wrong')
            return redirect('home')

    return redirect('home')


def addimage_view(request):
    forms = ImageForm()

    if request.method == 'POST':
        forms = ImageForm(request.POST , request.FILES)

        if forms.is_valid():
            forms.save()
            messages.success(request , 'Successfully Image Upload')
            return redirect('gallery')


        else:
            messages.warning(request , 'Something went wrong..')
            return redirect('addimage')


    context = {'forms':forms}
    return render(request , 'GalleryApp/addimage.html',context)

def signout_view(request):
    logout(request)
    messages.success(request , 'User Successfully LogOut')
    return redirect('home')
