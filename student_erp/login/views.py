from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from studentApp import views

def loginPage(request):
	if request.user.is_authenticated:
		return views.indexPage(request)
	else:
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
			if request.user.is_authenticated:
				return views.indexPage(request)

	return render(request,'home/Login_home.html',{})



def about(request):
	return render(request,'about/about.html',{})