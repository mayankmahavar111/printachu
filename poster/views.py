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
from .models import UserProfile,ArtistProfile,CustomerProfile,Category,poster
from django.core.mail import send_mail,mail_managers
from django.conf import settings
from .forms import FileFieldForm,PosterForm
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect


def artist(x,request,email):
	if x == True:
		artist = ArtistProfile.objects.create(
			user=request.user,
			name=User.first_name
		)
		artist.save()
		category=Category.objects.create(
			user=request.user
		)
		category.save()
		return redirect('/poster/profile')
	else:
		customer=CustomerProfile.objects.create(
			user=request.user,
			email=email
		)
		customer.save()
		return redirect('/poster/')

def mail(email,y):
	subject='KalaCircle'
	from_email=settings.EMAIL_HOST_USER
	to_email=email

	send_mail(
		subject,
		'You have succesfully registered in kalacircle. We will Keep updating you.'+y,
		from_email,
		[to_email],
		fail_silently=False
	)

	return
@csrf_exempt
@csrf_protect
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

			artist( x.join_as=="artist",request,email)

			mail(email,password1)
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
		try:
			x=UserProfile.objects.get(user=request.user)
		except:
			pass
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

def category(request):
	return render(request,'poster/category.html',{'Categorys': Category.objects.all()})

def anime(request):
	anime=poster.objects.filter(category__name='anime',user=request.user)
	return render(request,'poster/progress.html',{'anime':anime})

def people(request):
	return render(request, 'poster/progress.html')

def movies(request):
	return render(request, 'poster/progress.html')

def quotes(request):
	return render(request, 'poster/progress.html')

def sports(request):
	return render(request, 'poster/progress.html')

def nature(request):
	return render(request, 'poster/progress.html')


class Upload(FormView):
	form_class = FileFieldForm
	template_name = 'poster/upload.html'  # Replace with your template.
	success_url = 'poster/category'  # Replace with your URL or reverse().

	def post(self, request, *args, **kwargs):
		x=0
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		files = request.FILES.getlist('file_field')
		if form.is_valid():
			for f in files:
				post=poster.objects.create(
					user=request.user,
					name='anime',
					desription='mayank'+str(x),
					image=f
				)
				post.save()
				x=x+1
			return self.form_valid(form)
		else:
			return self.form_invalid(form)
	def get(self, request, *args, **kwargs):
		form=FileFieldForm()
		return render(request,'poster/upload.html',{'form':form})

def PosterUpload(request):
	if request.method=="POST":
		form=PosterForm(request.POST,request.FILES)
		user=UserProfile.objects.get(user=request.user)
		if form.is_valid():
			Cat=form.cleaned_data['category']
			desc=form.cleaned_data['description']
			Title=form.cleaned_data['title']
			imag=form.cleaned_data['image']
			post=poster.objects.create(
				user=request.user,
				category=Cat,
				title=Title,
				description=desc,
				image=imag
			)
			post.save()
			return redirect('/poster/category/'+str(form.cleaned_data['category']))
		else:
			return redirect('/poster/category/upload/')
	else:
		form=PosterForm()
		return render(request,'poster/upload.html',{'form':form})