from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from authnapp.forms import HabrUserLoginForm


def login(request):
    title = "Вход в систему"

    login_form = HabrUserLoginForm(data=request.POST or None)

    if request.method == "POST" and login_form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user and user.is_active:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("index"))

    content = {"title": title, "login_form": login_form}
    return render(request, "authnapp/login.html", content)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("index"))
