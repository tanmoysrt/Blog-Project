from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def homepage(request):

    data = "<h1>Hello World !!</h1>"
    return render(request,"normaluser/app.html",{"data":data})
