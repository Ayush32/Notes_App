from django.shortcuts import render
from django.http import HttpResponse
from base.models import User


# step 1 - create first view use from django.http import HttpResponse 
def index(request):
    # first view response
    # retreive data from model User
    data = User.objects.all()
    context = {
        'data' : data
    }
    print(data)
    return render(request,"home.html",context)
     
     
