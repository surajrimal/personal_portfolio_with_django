from django.shortcuts import render

# Create your views here.

def suraj(request):
    return render(request, 'jobs/home.html')