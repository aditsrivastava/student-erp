from django import forms

class loginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=100)
	password = forms.CharField(
		label='password',
		min_length=8,
		max_length=100
	)