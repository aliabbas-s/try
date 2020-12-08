from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateUserForm
from django.shortcuts import redirect
# Create your view;s here.
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


def index(request):
    return render(request, "zodo/index.html")


def main(request):
    return render(request, "zodo/main.html")


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            messages.info(request, "Username or Password is Incorrect")
    context = {}
    return render(request, "accounts/login.html", context)


def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {"form": form}
    return render(request, "accounts/register.html", context)
