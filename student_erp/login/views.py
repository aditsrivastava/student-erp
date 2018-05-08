from django.shortcuts import render

# Create your views here.

def loginPage(request):
	return render(request,'home/Login_home.html',{})

def about(request):
	return render(request,'about/about.html',{})