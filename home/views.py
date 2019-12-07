from django.shortcuts import render


def home_view(request):
    context = {
        "title": "Home"
    }
    return render(request, "home/home.html", context)


def about_view(request):
    context = {
        "title": "About Us"
    }
    return render(request, "home/about.html", context)


def contact_view(request):
    context = {
        "title": "Contact Us"
    }
    return render(request, "home/contact.html", context)


def term_view(request):
    context = {
        "title": "Terms and Conditions"
    }
    return render(request, "home/terms.html", context)
