from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class StudentData(models.Model):
	name = models.ForeignKey(User)
	rollNumber	= models.IntegerField()
	dob 		= models.DateField()
	email 		= models.EmailField()
	contectNo	= models.CharField(max_length=10)
	address		= models.CharField(max_length=150)
	city		= models.CharField(max_length=40)
	country		= models.CharField(max_length=40)

	#Parents Details 
	father_name			= models.CharField(max_length=100)
	father_email		= models.EmailField()
	father_contectNo	= models.CharField(max_length=10)

	mother_name			= models.CharField(max_length=100)
	mother_email		= models.EmailField()
	mother_contectNo	= models.CharField(max_length=10)