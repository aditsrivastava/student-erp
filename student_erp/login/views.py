from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.

def loginPage(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)

	if request.user.is_authenticated:
		print(True)
		return render(request,'home/home.html',{})
	else:
		print(False)
	return render(request,'home/Login_home.html',{})



def about(request):
	return render(request,'about/about.html',{})