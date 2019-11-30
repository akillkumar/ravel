from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

def register (response):

    if response.method == "POST": 
         login_form = RegisterForm(response.POST)
         if login_form.is_valid():
             login_form.save()
         
         return redirect('/myapp')         

    else:
        login_form = RegisterForm()

    return render(response, "register/register.html", {'login_form': login_form} )