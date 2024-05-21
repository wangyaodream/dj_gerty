from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, LoginForm
from .models import Record


def home(request):

    return render(request, "webapp/index.html", {})


# Register
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webapp:my-login')
    
    context = {'form': form}

    return render(request, "webapp/register.html", context=context)


# login a user
def my_login(request):
    
    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                # 定位到dashboard
                return redirect("webapp:dashboard")
    
    context = {'form': form}
    return render(request, "webapp/my-login.html", context=context)


def user_logout(request):
    auth.logout(request)
    return redirect("webapp:my-login")


@login_required(login_url='my-login')
def dashboard(request):
    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, "webapp/dashboard.html", context=context)
