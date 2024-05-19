from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm


def home(request):

    return render(request, "webapp/index.html", {})


# Register
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webapp/home.html')
    
    context = {'form': form}

    return render(request, "webapp/register.html", context=context)
