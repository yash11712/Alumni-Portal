from django.shortcuts import render


def base(request):
    return render(request, 'home/home.html')
