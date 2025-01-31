from django.shortcuts import render

def home(request):
    return render(request, 'planner/index.html')