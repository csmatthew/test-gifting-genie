from django.shortcuts import render


def myaccount_home(request):
    return render(request, 'myaccount/home.html')
