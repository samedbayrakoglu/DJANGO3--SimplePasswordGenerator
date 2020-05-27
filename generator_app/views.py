from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator_app/index.html')


def about(request):
    return render(request, 'generator_app/about.html')


def password(request):
    characters = list('abcdefghjklmnoprstuvywz')

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*?'))

    if length < 6 or length > 12:
        return HttpResponse('Please provide a valid password length!!')

    mypassword = ''
    for x in range(length):
        mypassword += random.choice(characters)
    return render(request, 'generator_app/password.html', {'password': mypassword})