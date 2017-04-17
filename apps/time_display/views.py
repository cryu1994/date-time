from django.shortcuts import render, redirect
import datetime
now = datetime.datetime.now()

def index(request):
    context = {
        "now": now
    }
    return render(request, "index/index.html")
