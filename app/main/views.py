# app/main/views.py
from django.shortcuts import render

# Create your views here.

# Home page
def frontHome(request):
	return render(request, 'main/front-home.html')

# About page
def frontAbout(request):
	return render(request, 'main/front-about.html')