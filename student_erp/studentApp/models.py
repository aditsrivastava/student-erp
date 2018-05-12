from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class StudentData(models.Model):
	name = models.ForeignKey(User)
	dob = models.DateField()