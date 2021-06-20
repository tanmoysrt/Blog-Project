from django.http import HttpResponse
from django.shortcuts import render

def homepage(request,titile):
    print("HI")
    print(titile)
    return render(request,"normaluser/app.html",{"titile":titile,"name":"tanmoy Sarkar"})
