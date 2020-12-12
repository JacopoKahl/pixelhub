from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog

# Create your views here.

#https://www.udemy.com/course/python-django-tkinter-complete-bundle-advance/learn/lecture/16516338#overview

def home(request):

    return render(request, 'home.html')