from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from .models import UserProfile,ArtistProfile,poster
from django.utils import timezone

STATUS_CHOICES= (
    (1, ("Artist")),
    (2, ("Customer")),
)
Gender=(
    (1, ("Male")),
    (2, ("Female")),
)

class RegistrationForm(forms.Form):
    first_name = forms.CharField(required=True, label='First Name')
    last_name=forms.CharField(required=True,label='Last name')
    email=forms.EmailField(required=True,label='Your Email ID ')
    #username=forms.CharField(required=True,label='Usesrname ',initial='username')
    dob=forms.DateField(required=True,initial=timezone.now(),label='Date of Birth',)
    gender=forms.ChoiceField(required=True,label="Gender ",choices=Gender)
    password1=forms.CharField(required=True,widget=forms.PasswordInput,label='Password')
    password2 = forms.CharField(required=True, widget=forms.PasswordInput,label='Password(again)')
    type=forms.ChoiceField(choices=STATUS_CHOICES,required=True,widget=None,label=None,initial="",)

    class Meta:
        model=User
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1'
            'password2'

        )

class ArtistProfileForm(forms.ModelForm):
    class Meta:
        model=ArtistProfile
        fields=(

            'profile_pic',
            'background_pic',
            'Description',


        )

class PosterForm(forms.ModelForm):
    tags=forms.CharField(required=True)
    class Meta :
        model=poster
        fields=(
            'title',
            'description',
            'category',
            'image',
            'tags'

        )

class SearchForm(forms.Form):
    search=forms.CharField(label="Search ")
