from django.shortcuts import render
from .models import MyAccount

def myaccount_home(request):
    myaccount = MyAccount.objects.first()
    return render(request, 'myaccount/profile.html', {'myaccount': myaccount})
