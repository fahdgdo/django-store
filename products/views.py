from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


# Create your views here.

def say_hi(request, name):
    return render(request, 'say-hi.html', {'name':name})


def show_time(request, name):
    now = timezone.now()
    form_now=now.strftime("%A, %d %B, %Y at %X")
    #time={'now':now}
    #return HttpResponse('show-time.html', form_now)
    return render(request, 'show-time.html', {'name':form_now})