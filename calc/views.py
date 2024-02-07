from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Susan'})

def result(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    add = val1 + val2

    return render(request, 'result.html', {'result': add})
