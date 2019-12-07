from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpRequest
import socket


from .models import Message


def submit_view(request, receiver):

    check = User.objects.filter(username=receiver).count()
    if check == 0:
        return redirect('/')

    if request.method == "POST":
        to = receiver
        message = request.POST.get('msg')

        invalid_list = ["pussy", "dick", "fuck", "tit", "boobs", "tits", "bokachoda", "madarchod", "randi", "vagina", "behenchod", "benchod", "cod", "chut"]
        for invalid_word in invalid_list:
            if invalid_word in message:
                return redirect("/error/")
        print(to, message)
        Message.objects.create(to=to, message=message)
        return redirect("/success/")

    context = {
        "title": "Submit",
        "to": receiver,
    }

    return render(request, "submit/submit.html", context)


def success_view(request):
    return render(request, "submit/success.html", {"title": "Success"})


def error_view(request):
    return render(request, "submit/error.html", {"title": "Error"})


def return_home(request):
    return redirect("/")
