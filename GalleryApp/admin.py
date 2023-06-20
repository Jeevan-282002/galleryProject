from django.contrib import admin
from . models import CategoryModel , ImageModel

# Register your models here.


@admin.register(CategoryModel)
class CategoryModel(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ImageModel)
class ImageModel(admin.ModelAdmin):
    list_display = ['img_title' , 'image' , 'category']
