from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from poster.forms import RegistrationForm
from django.views.generic import TemplateView
from django.views import  generic
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

def saveRegister(request):
	if request.method == "POST":
		print request.POST
		first_name=request.POST.get('firstname')
		last_name=request.POST.get('lastname')
		email=request.POST.get('email')
		password1=request.POST.get('password1')
		password2=request.POST.get('password2')
		dob=request.POST.get('dateofbirth')
		gender=request.POST.get('gender')
		type=request.POST.get('usertype')
		User.objects.create(
			username= first_name,
			email=email,
			password=password1,
		)
		print first_name,last_name,email,password1,password2,dob,gender,type
		return redirect('/poster/test2')
	else:
		print "hello world"
		return render(request,'poster/register.html')

def test2(request):
	if request.method == "POST":
		print request.POST
		x=request.POST.get('x')
		y=request.POST.get('y')
		print x,y
		return redirect('/poster')
	else:
		return render(request,'poster/test.html')

def test(request,your_name,last_name):

		print your_name,last_name
		return redirect('/poster/test2')
def register(request):
		return render(request,'poster/register.html')

@login_required
def profile(request):
	return render(request,'poster/profile.html')

@method_decorator(login_required, name='dispatch')
class Profile(TemplateView):
	template_name = 'poster/profile.html'



class Index(TemplateView):
	template_name = 'poster/home.html'

