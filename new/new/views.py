from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import *

def home(req):
    about_me_data = AboutMe.objects.get(id = 1)
    data = {'d' : about_me_data}
   
    return render(req,'index.html')

def about_me(req):
    return render(req,'about_me.html')

def about_meInsert(req):
    name = req.POST.get('name')
    age = req.POST.get('age')
    occupation = req.POST.get('occupation')
    phone = req.POST.get('phone')
    email = req.POST.get('email')
    nationality = req.POST.get('nationality')
    description = req.POST.get('description')

    about_me_obj = AboutMe()

    about_me_obj.name = name
    about_me_obj.age = age
    about_me_obj.occupation = occupation
    about_me_obj.phone = phone
    about_me_obj.email = email
    about_me_obj.nationality = nationality
    about_me_obj.description = description

    about_me_obj.save()

    return HttpResponse(name)

