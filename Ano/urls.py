from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from home.views import home_view, contact_view, about_view, term_view
from accounts.views import login_page, register_page
from dashboard.views import dashboard_view
from submit.views import success_view, error_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('login/', login_page, name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('registration/', register_page, name="register"),
    path('dashboard/', dashboard_view, name="dash"),
    path('contact/', contact_view, name="contact"),
    path('success/', success_view, name="success"),
    path('error/', error_view, name="error"),
    path('about/', about_view, name="about"),
    path('terms/', term_view, name="terms"),
    url(r'^submit/', include(('submit.urls', 'submit'), namespace='submit')),
]
