from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# Create your models here.


class CreateUserForm(UserCreationForm):
    email=forms.CharField(label="Email")
    class Meta:
        model=User
        fields = ['first_name','username','email', 'password1','password2']
        #User._meta.get_field('email').unique=True
        
