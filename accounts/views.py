from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from .forms import LoginForm, RegisterForm


def login_page(request):
    if request.user.is_authenticated:
        return redirect("/dashboard/")
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard/")
        else:
            print("Error")
            context["error"] = "Username and Password do not match!"
    return render(request, "accounts/login.html", context)


User = get_user_model()


def register_page(request):
    if request.user.is_authenticated:
        return redirect("/dashboard/")
    form = RegisterForm(request.POST or None)
    context = {
        "title": "Login",
        "content": "Login",
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        f_name = name[0]
        l_name = name[1]

        User.objects.create_user(
            username, email, password,
            first_name=f_name,
            last_name=l_name, )
        return redirect('/login/')

    return render(request, "accounts/register.html", context)
