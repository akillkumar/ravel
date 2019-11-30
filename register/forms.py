from django import forms
from django.db import models
from datetime import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm (UserCreationForm):
    email = models.EmailField ()

    class Meta:
        model = User
        # username, pwd1, and pwd2 already exist
        # add others in the order we want
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
