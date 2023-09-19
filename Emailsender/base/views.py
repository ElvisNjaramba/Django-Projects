from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail


def send_email(request):
    send_mail(
        'Welcome Home',
        'Hello welcome to tm space',
        'example@gmail.com',
        ['example@gmail.com'],
        fail_silently=False,
    )
    return render(request, 'base/index.html')

