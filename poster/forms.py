from django import forms
from django.contrib.auth.forms import format_html
from django.contrib.auth.models import User
from .models import UserProfile,ArtistProfile,poster
from django.contrib.auth.forms import UserCreationForm



class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True,label='Your Email ID: - ',initial='email')
    first_name=forms.CharField(required=True,label='Your Name:')
    username=forms.CharField(required=True,label='Usesrname ',initial='username')
    dob=forms.DateField(required=True,label='Date of Birth')
    gender=forms.CharField(required=True,label="Gender ")

    class Meta:
        model=User
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'

        )


class ArtistProfileForm(forms.ModelForm):
    class Meta:
        model=ArtistProfile
        fields=(

            'profile_pic',

            'Description',


        )

class PosterForm(forms.ModelForm):
    class Meta :
        model=poster
        fields=(
            'title',
            'description',
            'category',
            'image'

        )

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))