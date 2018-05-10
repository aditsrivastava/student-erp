from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import logout

from login import views
# Create your views here.

def indexPage(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			logoutU = request.POST.get('logout')
			if logoutU=='Logout':
				logout(request)
				return views.loginPage(request)

		return render(request,'home/index.html',{'user':request.user})
	else:
		return views.loginPage(request)		