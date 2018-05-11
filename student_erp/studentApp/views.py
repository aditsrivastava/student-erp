from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.

@login_required(login_url='/')
def indexPage(request):
	return render(request,'home/index.html',{'user':request.user})

@login_required(login_url='/')
def attendence(request):
	return render(request,'userInteraction/attendence.html',{'user':request.user})


def logoutView(request):
	if request.user.is_authenticated:
		logout(request)
		return redirect('/')