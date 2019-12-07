from django.shortcuts import render, redirect
from submit.models import Message


def dashboard_view(request):
    if request.user.is_authenticated:
        url = "localhost:8000/submit/" + request.user.username
        messages = Message.objects.filter(to=request.user.username).order_by("-timestamp")
        context = {
            "title": "Dashboard",
            "url": url,
            "messages": messages,
        }
        return render(request, "dash/dash.html", context)
    else:
        return redirect("/login/")
