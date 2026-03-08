from django.shortcuts import render

def sign_in(request):
    return render(request, 'login.html')

def login(request):
    return render(request, 'login.html')