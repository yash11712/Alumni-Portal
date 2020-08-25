from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def register(request):
    return render(request, 'home/register1.html')


def register2(request):
    return render(request, 'home/registerfinal.html')


def login(request):
    return render(request, 'home/home.html')
