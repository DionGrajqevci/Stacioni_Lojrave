from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/products/")
        ...
    else:
        messages.success(request, "There was a error logging in,try again!")
        return redirect("login")

def logout_user(request):
    logout(request)
    messages.success(request, "You logged out!")
    return redirect("/users/login/")


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log in the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
    
            return redirect('/products/')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/register.html', {'form': form})



        