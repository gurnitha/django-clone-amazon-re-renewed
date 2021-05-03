# app/backend/views.py
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
'''import login_required module to add conditionl to user login'''
from django.contrib.auth.decorators import login_required

# Create your views here.

# Admi home
'''Only loggeg in user can access the admin dashboard'''
@login_required(login_url='/admin/login')
def adminHome(request):
	return render(request, 'backend/admin-home.html')

# Admi login
def adminLogin(request):
	return render(request, 'backend/admin-login.html')

# Admin login process
def adminLoginProcess(request):
	# Get input from the login form
	username=request.POST.get('username')
	password=request.POST.get('password')

	# Authenticate user credentials
	user=authenticate(
		request=request,
		username=username,
		password=password)

	# If user exist
	if user is not None:
		login(request=request, user=user)
		return HttpResponseRedirect(reverse('admin_home'))
	# If user not exist
	else:
		messages.error(
			request, 'Login error! Invalid login detail!')
		return HttpResponseRedirect(reverse('admin_login'))

# Admin logout process
def adminLogoutProcess(request):
	logout(request)
	messages.success(request, 'Logged out successfully!')
	return HttpResponseRedirect(reverse('admin_login'))		