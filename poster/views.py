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


def test(request):
	if request.method == "GET":
		return render(request,'poster/test.html')

def register(request):
	print 'Hello World'
	if request.method=='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/poster/login')
		else:
			return redirect('/poster/register')
	else :
		form=RegistrationForm()
		args={'form':form}
		return render(request,'poster/register.html',args)

@login_required
def profile(request):
	return render(request,'poster/profile.html')

@method_decorator(login_required, name='dispatch')
class Profile(TemplateView):
	template_name = 'poster/profile.html'



class Index(TemplateView):
	template_name = 'poster/home.html'

