from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import StudentData

# Create your views here.

@login_required(login_url='/')
def indexPage(request):
	sdData = StudentData.objects.all().values()[0]
	del sdData['id']
	del sdData['name_id']
	sdData = sdData.items()

	return render(
		request,
		'home/index.html',
		{
			'user':request.user,
			'SD':sdData
		}
	)

@login_required(login_url='/')
def attendence(request):
	return render(request,'userInteraction/attendence.html',{'user':request.user})


def logoutView(request):
	if request.user.is_authenticated:
		logout(request)
		return redirect('/')