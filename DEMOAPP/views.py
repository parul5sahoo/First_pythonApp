from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'DEMOAPP/login_forms.html')

def submit(request):
    return HttpResponse('WELCOME')
