from django.shortcuts import render


def home_view(request):
    context = {
        "title": "Home"
    }
    return render(request, "home/home.html", )


def about_view(request):
    context = {
        "title": "About Us"
    }
    return render(request, "home/about.html", )


def contact_view(request):
    context = {
        "title": "Contact Us"
    }
    return render(request, "home/contact.html", )


def term_view(request):
    context = {
        "title": "Home"
    }
    return render(request, "home/terms.html", )
