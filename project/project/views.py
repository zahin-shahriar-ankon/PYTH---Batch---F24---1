from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import *

def home(req):
    about_me_data = AboutMe.objects.get(id = 3)
    intro_data = Intro.objects.get(id = 1)
    works_data = Works.objects.get(id = 1)
    data = {'d' : about_me_data, 'i' : intro_data, 'w' : works_data}
    return render(req,'index.html',data)

def intro(req):
    return render(req,'intro.html')

def introInsert(req):
    name = req.POST.get('i_name')
    occupation = req.POST.get('i_occupation')

    intro_obj = Intro()

    intro_obj.i_name = name
    intro_obj.i_occupation = occupation

    intro_obj.save()

    return redirect('intro_admin')

def works(req):
    return render(req,'works.html')

def worksInsert(req):
    name_one = req.POST.get('w_name_box_1')
    description_one = req.POST.get('w_description_box_1')
    name_two = req.POST.get('w_name_box_2')
    description_two = req.POST.get('w_description_box_2')
    name_three = req.POST.get('w_name_box_3')
    description_three = req.POST.get('w_description_box_3')
    name_four = req.POST.get('w_name_box_4')
    description_four = req.POST.get('w_description_box_4')

    works_object = Works()

    works_object.w_name = name
    works_object.w_description = description

    works_object.save()

    return redirect('works_admin')

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

    about_obj = AboutMe()

    about_obj.name = name
    about_obj.age = age
    about_obj.occupation = occupation
    about_obj.phone = phone
    about_obj.email = email
    about_obj.nationality = nationality
    about_obj.description = description

    about_obj.save()

    return redirect('about_me_admin')