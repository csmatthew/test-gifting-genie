from django.urls import path
from . import views

urlpatterns = [
    path('', views.myaccount_home, name='myaccount'),
]