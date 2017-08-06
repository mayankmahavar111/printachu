from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import decorators
from poster.forms import ArtistProfileForm
from django.views.generic import TemplateView
from django.views import  generic
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User,UserManager
from django.contrib.auth import authenticate,login
from .models import UserProfile,ArtistProfile,CustomerProfile,Category,poster,tags
from django.core.mail import send_mail,mail_managers
from django.conf import settings
from .forms import SearchForm,PosterForm,RegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from payments import get_payment_model, RedirectNeeded
from decimal import Decimal
from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, Template,RequestContext
import datetime
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators import csrf

from payments import get_payment_model

def artist(x,request,email):
	if x == True:
		artist = ArtistProfile.objects.create(
			user=request.user,
			name=User.first_name
		)

		artist.save()

		print "Hello World"

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


def saveRegister(request):
	if request.method == "POST":
		form=RegistrationForm(request.POST)
		print request.POST
		if form.is_valid():
			first_name=form.cleaned_data['first_name']
			last_name=form.cleaned_data['last_name']
			email=form.cleaned_data['email']
			password1=form.cleaned_data['password1']
			password2=form.cleaned_data['password2']
			dob=form.cleaned_data['dob']
			gender=form.cleaned_data['gender']
			type=form.cleaned_data['type']
			if gender=='1':
				gender="Male"
			else:
				gender ="Female"
			if type=='1':
				type="artist"
			else:
				type="customer"
		else:
			pass
		try:
			user=User.objects.create(
				username=email,
				email=email,
				password=password1,
			)
		except:
			return redirect('/poster/register/')

		user.set_password(password1)
		user.save()
		user=authenticate(username=email,password=password1)

		#print user
		try:
			if user is not None:
				print "hello"
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
				print " World"
				print first_name,last_name,email,password1,password2,dob,gender,type
				return redirect('/poster/login')

		except:
			x.delete()
			x=User.objects.get(username=email)
			x.delete()
			return redirect('/poster/')
	else:
		form=RegistrationForm()
		print "hello world"
		return render(request,'poster/register.html',{'form':form})



def test2(request):
	x=poster.objects.filter(user=request.user,title__contains="naruto")
	return render(request,'poster/test.html',{'x':x})

def test(request):
	email="mayank.mahavar@shephertz.co.in"
	y="abcdefg"
	mail(email,y)
	return redirect('/poster/test2')
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
			print request.user
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


@login_required()
def createprofile(request):
	if request.method=="POST":
		x=ArtistProfile.objects.get(user=request.user)
		form=ArtistProfileForm(request.POST,request.FILES)
		print "Hello"
		if form.is_valid():
			print "World"
			x.profile_pic=form.files['profile_pic']
			x.background_pic=form.files['background_pic']
			x.Description=form.cleaned_data['Description']
			x.about=form.cleaned_data['about']
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
	Category=poster.objects.filter(category__name='anime',user=request.user)
	return render(request,'poster/progress.html',{'anime':Category})

def people(request):
	Category = poster.objects.filter(category__name='people', user=request.user)
	return render(request, 'poster/progress.html', {'anime': Category})

def movies(request):
	Category = poster.objects.filter(category__name='movies', user=request.user)
	return render(request, 'poster/progress.html', {'anime': Category})

def quotes(request):
	Category = poster.objects.filter(category__name='quotes', user=request.user)
	return render(request, 'poster/progress.html', {'anime': Category})

def sports(request):
	Category = poster.objects.filter(category__name='sports', user=request.user)
	return render(request, 'poster/progress.html', {'anime': Category})

def nature(request):
	Category = poster.objects.filter(category__name='nature', user=request.user)
	return render(request, 'poster/progress.html', {'anime': Category})

def display(request,id):
	if request.method=="POST":
		user=UserProfile.objects.get(user=request.user)
		#print id
		if user.cart is None:
			user.cart = id
		else:
			user.cart = user.cart + " " + id
		#print user.cart
		user.save()
		return redirect('/poster/designs')
	else:
		pos=poster.objects.filter(id=id)
		return render(request,'poster/display.html',{'poster':pos})


def PosterUpload(request):
	if request.method=="POST":
		form=PosterForm(request.POST,request.FILES)
		user=UserProfile.objects.get(user=request.user)
		if form.is_valid():
			desc=form.cleaned_data['description']
			Title=form.cleaned_data['title']
			imag1=form.cleaned_data['image1']
			imag2=form.cleaned_data['image2']
			imag3=form.cleaned_data['image3']
			post=poster.objects.create(
				user=request.user,
				category='all',
				title=Title,
				description=desc,
				image1=imag1,
				image2=imag2,
				imag3=imag3,
			)
			if tags.objects.filter(title=form.cleaned_data['tags']) is False:
				tag=tags.objects.create(
					title=form.cleaned_data['tags']
				)
			else:
				tag=tags.objects.get(title=form.cleaned_data['tags'])

			x= (tag.poster_name+" "+Title)
			print x
			tag.poster_name=tag.poster_name+" "+str(Title)
			post.save()
			tag.save()
			return redirect('/poster/category/'+str(form.cleaned_data['category']))
		else:
			return redirect('/poster/category/upload/')
	else:
		form=PosterForm()
		return render(request,'poster/upload.html',{'form':form})


def search(request):
	if request.method=="POST":
		form=SearchForm(request.POST)
		tag=form.cleaned_data['search'].split(" ")
		for t in tag:
			if tags.objects.filter(title=t) :
				x=tags.objects.get(title=t)
				a=a+x.poster_name.split(" ")
			else:
				return render(request,'poster/not_found.html')
		print a
		poster=""
		for p in a:
			if p in poster:
				pass
			else:
				poster=poster+" "+p

	else:
		form=SearchForm()
		return render(request,'poster/Search.html',{'form':form})


def payment_details(request, payment_id):
	payment = get_object_or_404(get_payment_model(), id=payment_id)
	try:
		form = payment.get_form(data=request.POST or None)
	except RedirectNeeded as redirect_to:
		return redirect(str(redirect_to))
	return TemplateResponse(request, 'poster/payment.html',{'form': form, 'payment': payment})

Payment = get_payment_model()
payment = Payment.objects.create(
    variant='default',  # this is the variant from PAYMENT_VARIANTS
    description='Book purchase',
    total=Decimal(120),
    tax=Decimal(20),
    currency='USD',
    delivery=Decimal(10),
    billing_first_name='Sherlock',
    billing_last_name='Holmes',
    billing_address_1='221B Baker Street',
    billing_address_2='',
    billing_city='London',
    billing_postcode='NW1 6XE',
    billing_country_code='UK',
    billing_country_area='Greater London',
    customer_ip_address='127.0.0.1')



def Home(request):
	MERCHANT_KEY = "JBZaLc"
	key = "JBZaLc"
	SALT = "GQs7yium"
	PAYU_BASE_URL = "https://test.payu.in/_payment"
	action = ''
	posted = {}
	for i in request.POST:
		posted[i] = request.POST[i]
	hash_object = hashlib.sha256(b'randint(0,20)')
	txnid = hash_object.hexdigest()[0:20]
	hashh = ''
	posted['txnid'] = txnid
	hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
	posted['key'] = key
	hash_string = ''
	hashVarsSeq = hashSequence.split('|')
	for i in hashVarsSeq:
		try:
			hash_string += str(posted[i])
		except Exception:
			hash_string += ''
		hash_string += '|'
	hash_string += SALT
	hashh = hashlib.sha512(hash_string).hexdigest().lower()
	action = PAYU_BASE_URL
	if (posted.get("key") != None and posted.get("txnid") != None and posted.get("productinfo") != None and posted.get(
			"firstname") != None and posted.get("email") != None):
		return render_to_response('poster/current_datetime.html', RequestContext(request, {"posted": posted, "hashh": hashh,
																					"MERCHANT_KEY": MERCHANT_KEY,
																					"txnid": txnid,
																					"hash_string": hash_string,
																					"action": "https://test.payu.in/_payment"}))
	else:
		return render_to_response('poster/current_datetime.html', RequestContext(request, {"posted": posted, "hashh": hashh,
																					"MERCHANT_KEY": MERCHANT_KEY,
																					"txnid": txnid,
																					"hash_string": hash_string,
																					"action": "."}))


@csrf_protect
@csrf_exempt
def success(request):
	c = {}
	c.update(csrf(request))
	status = request.POST["status"]
	firstname = request.POST["firstname"]
	amount = request.POST["amount"]
	txnid = request.POST["txnid"]
	posted_hash = request.POST["hash"]
	key = request.POST["key"]
	productinfo = request.POST["productinfo"]
	email = request.POST["email"]
	salt = "GQs7yium"
	try:
		additionalCharges = request.POST["additionalCharges"]
		retHashSeq = additionalCharges + '|' + salt + '|' + status + '|||||||||||' + email + '|' + firstname + '|' + productinfo + '|' + amount + '|' + txnid + '|' + key
	except Exception:
		retHashSeq = salt + '|' + status + '|||||||||||' + email + '|' + firstname + '|' + productinfo + '|' + amount + '|' + txnid + '|' + key
	hashh = hashlib.sha512(retHashSeq).hexdigest().lower()
	if (hashh != posted_hash):
		print "Invalid Transaction. Please try again"
	else:
		print "Thank You. Your order status is ", status
		print "Your Transaction ID for this transaction is ", txnid
		print "We have received a payment of Rs. ", amount, ". Your order will soon be shipped."
	return render_to_response('poster/sucess.html',
							  RequestContext(request, {"txnid": txnid, "status": status, "amount": amount}))


@csrf_protect
@csrf_exempt
def failure(request):
	c = {}
	c.update(csrf(request))
	status = request.POST["status"]
	firstname = request.POST["firstname"]
	amount = request.POST["amount"]
	txnid = request.POST["txnid"]
	posted_hash = request.POST["hash"]
	key = request.POST["key"]
	productinfo = request.POST["productinfo"]
	email = request.POST["email"]
	salt = "GQs7yium"
	try:
		additionalCharges = request.POST["additionalCharges"]
		retHashSeq = additionalCharges + '|' + salt + '|' + status + '|||||||||||' + email + '|' + firstname + '|' + productinfo + '|' + amount + '|' + txnid + '|' + key
	except Exception:
		retHashSeq = salt + '|' + status + '|||||||||||' + email + '|' + firstname + '|' + productinfo + '|' + amount + '|' + txnid + '|' + key
	hashh = hashlib.sha512(retHashSeq).hexdigest().lower()
	if (hashh != posted_hash):
		print "Invalid Transaction. Please try again"
	else:
		print "Thank You. Your order status is ", status
		print "Your Transaction ID for this transaction is ", txnid
		print "We have received a payment of Rs. ", amount, ". Your order will soon be shipped."
	return render_to_response("poster/Failure.html", RequestContext(request, c))

def cart(request):
	if request.method=="POST":
		pass
	else:
		if not User.is_authenticated:
			return redirect('/poster/login')
		user=UserProfile.objects.get(user=request.user)
		x=user.cart.split(" ")
		dic={}
		for i in x[1:]:
			i=int(i)
			try:
				dic[i]=dic[i]+1
			except:
				dic[i]=1
		print dic[2]
		design=poster.objects.filter(pk__in=x[1:])
		temp=0
		return render(request,'poster/cart.html',{'anime':design,'dic':dic,'x':temp})

def order(request):
	if request.method=="POST":
		pass
	else:
		return render(request,'poster/order.html')

def allDesigns(request):
	Category = poster.objects.all()
	return render(request, 'poster/progress.html', {'anime': Category})

login_required()
def all(request):
	Category=poster.objects.filter(user=request.user)

def about(request):
	return render(request,'poster/about.html')