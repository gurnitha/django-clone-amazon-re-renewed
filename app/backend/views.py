# app/backend/views.py
from django.shortcuts import render

# Create your views here.

# Admi home
def adminHome(request):
	return render(request, 'backend/admin-home.html')

# Admi login
def adminLogin(request):
	return render(request, 'backend/admin-login.html')