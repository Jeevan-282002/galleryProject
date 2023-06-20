from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view , name = 'home'),
    path('gallery/',views.gallery_view , name = 'gallery'),
    path('signup/',views.signup_view , name = 'signup'),
    path('signin/',views.signin_view , name = 'signin'),
    path('addimage/',views.addimage_view , name = 'addimage'),
    path('signout/',views.signout_view , name = 'signout'),
    path('catimage/<int:id>' , views.catimage_view , name = 'catimage'),

]