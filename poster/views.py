from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from poster.forms import ArtistProfileForm
from django.views.generic import TemplateView
from django.views import  generic
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User,UserManager
from django.contrib.auth import authenticate,login
from .models import UserProfile,ArtistProfile,CustomerProfile
from django.core.mail import send_mail,mail_managers
from django.conf import settings


def mail(email):
	subject='KalaCircle'
	from_email=settings.EMAIL_HOST_USER
	to_email=email

	send_mail(
		subject,
		'You have succesfully registered in kalacircle. We will Keep updating you.',
		from_email,
		[to_email],
		fail_silently=False
	)

	return redirect('/poster/test2')

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
		try:
			user=User.objects.create(
				username=email,
				email=email,
				password=password1,
			)
		except:
			return redirect('/poster/register')

		user.set_password(password1)
		user.save()
		user=authenticate(username=email,password=password1)

		print user
		if user is not None:
			login(request, user)
			x=UserProfile.objects.create(
				user=email,
				first_name=first_name,
				last_name=last_name,
				email=email,
				date_of_birth=dob,
				join_as=type,
				gender=gender
			)
			x.save()

			if x.join_as=="artist":
				artist=ArtistProfile.objects.create(
					user=request.user,
					name=first_name
				)
				artist.save()
				mail(email)
				return redirect('/poster/profile')
			else:
				mail(email)
				return redirect('/poster/')
		print first_name,last_name,email,password1,password2,dob,gender,type
		return redirect('/poster/register')
	else:
		print "hello world"
		return render(request,'poster/register.html')

def test2(request):
	user=authenticate(username='testing',password='user@1234')
	if user is not None:
		login(request,user)
	return render(request,'poster/test.html')

def test(request,your_name,last_name):

		print your_name,last_name
		return redirect('/poster/test2')
def register(request):
		return render(request,'poster/register.html')

@login_required
def profile(request):

	if request.method=="POST":
		pass
	else:
		x=UserProfile.objects.get(user=request.user)
		if x.join_as=="artist":
			artist=ArtistProfile.objects.get(user=request.user)
			#print "Hello World"
			#print x.first_name,x.last_namex
			args={
				'x':x,
				'artist':artist
			}
			return render(request,'poster/profile.html',args)
		else:
			return redirect('/poster')
@method_decorator(login_required, name='dispatch')
class Profile(TemplateView):
	template_name = 'poster/profile.html'


@login_required()
def createprofile(request):
	if request.method=="POST":
		x=ArtistProfile.objects.get(user=request.user)
		form=ArtistProfileForm(request.POST,request.FILES)
		print "Hello"
		if form.is_valid():
			print "World"
			x.profile_pic=form.files['profile_pic']
			x.Description=form.cleaned_data['Description']
			x.save()
		return  redirect('/poster/profile')
	else:
		form=ArtistProfileForm()
		return render(request,'poster/buildprofile.html',{'form':form})

class Index(TemplateView):
	template_name = 'poster/home.html'

