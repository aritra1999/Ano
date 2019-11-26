from django.conf.urls import url
from django.urls import path

from .views import submit_view, success_view, return_home
from home.views import home_view

urlpatterns = [
    path('', return_home, name="return_home"),
    url(r'^(?P<receiver>[\w-]+)/$', submit_view, name='submit'),
]
