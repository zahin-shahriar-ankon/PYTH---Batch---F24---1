from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import *

def home(req):
    intro_data = Intro.objects.get(id = 1)
    works_data = Works.objects.all()
    about_me_data = AboutMe.objects.get(id = 1)
    edu_data = Education.objects.get(id = 1)
    deg_data = Degrees.objects.all()
    project_data = Project.objects.get(id = 1)
    a_project_data = AProject.objects.all()
    ex_data = Experience.objects.get(id = 1)
    a_ex_data = AExperience.objects.all()
    res_data = Research.objects.get(id = 1)
    a_res_data = AResearch.objects.all()
    ff_data = Fun.objects.get(id = 1)
    af_data =  AFact.objects.all()
    s_data = Skill.objects.get(id = 1)
    a_s_data = ASkill.objects.all()
    t_desc_data = Testimonial.objects.get(id = 1)
    f_data = Feedback.objects.all()
    srvc_t_data = Service.objects.get(id = 1)
    srvc_data = Services.objects.all()
    cntc_t_data = Contact.objects.get(id = 1)
    cntc_data = Contacts.objects.get(id = 1)

    data = {'i' : intro_data, 'w' : works_data, 'a' : about_me_data, 'e' : edu_data, 'd' : deg_data, 'p' : project_data, 'ap' : a_project_data, 'ex' : ex_data, 'a_ex' : a_ex_data, 'r' : res_data, 'ar' : a_res_data, 'ff' : ff_data, 'af' : af_data, 's' : s_data, 'as' : a_s_data, 't' : t_desc_data, 'f' : f_data, 'srvct' : srvc_t_data, 'srvc' : srvc_data, 'c' : cntc_t_data, 'cntc' : cntc_data} 

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
    works_title = req.POST.get('w_title') 
    works_description = req.POST.get('w_description')

    works_obj = Works()

    works_obj.w_title = works_title
    works_obj.w_description = works_description
    
    works_obj.save()

    return redirect('works_admin')

def about_me(req):
    return render(req,'about_me.html')

def about_meInsert(req):
    description = req.POST.get('a_description')
    name = req.POST.get('a_name')
    age = req.POST.get('a_age')
    occupation = req.POST.get('a_occupation')
    phone = req.POST.get('a_phone')
    email = req.POST.get('a_email')
    nationality = req.POST.get('a_nationality')

    about_me_obj = AboutMe()

    about_me_obj.a_description = description
    about_me_obj.a_name = name
    about_me_obj.a_age = age
    about_me_obj.a_occupation = occupation
    about_me_obj.a_phone = phone
    about_me_obj.a_email = email
    about_me_obj.a_nationality = nationality

    about_me_obj.save()

    return redirect('about_me_admin')

def edu(req):
    return render(req,'edu.html')   

def eduInsert(req):
    description = req.POST.get('e_description')

    edu_obj = Education()

    edu_obj.e_description = description

    edu_obj.save()

    return redirect('edu_admin') 

def deg(req):
    return render(req,'degrees.html')

def degInsert(req):
    title = req.POST.get('d_title')
    institution = req.POST.get('d_institution')
    duration = req.POST.get('d_duration')
    description = req.POST.get('d_description')

    deg_obj = Degrees()

    deg_obj.d_title = title
    deg_obj.d_institution = institution
    deg_obj.d_description = description
    deg_obj.d_duration = duration

    deg_obj.save()

    return redirect('deg_admin')

def project(req):
    return render(req,'project.html')

def projectInsert(req):
    description = req.POST.get('p_description')

    project_obj = Project()

    project_obj.p_description = description

    project_obj.save()

    return redirect('project_admin')

def a_project(req):
    return render(req,'a_project.html')

def a_projectInsert(req):
    description = req.POST.get('ap_description')

    a_project_obj = AProject()

    a_project_obj.ap_description = description

    a_project_obj.save()

    return redirect('a_project_admin')

def ex(req):
    return render(req,'experience.html')

def exInsert(req):
    description = req.POST.get('ex_description')

    ex_obj = Experiences()

    ex_obj.ex_description = description

    ex_obj.save()

    return redirect('ex_admin')

def a_ex(req):
    return render(req,'a_experience.html')

def a_exInsert(req):
    title = req.POST.get('a_ex_title')
    institution = req.POST.get('a_ex_institution')
    duration = req.POST.get('a_ex_duration')
    description = req.POST.get('a_ex_description')

    a_ex_obj = AExperience()

    a_ex_obj.a_ex_title = title
    a_ex_obj.a_ex_institution = institution
    a_ex_obj.a_ex_duration = duration
    a_ex_obj.a_ex_description = description

    a_ex_obj.save()

    return redirect('a_ex_admin')

def res(req):
    return render(req,'research.html')

def resInsert(req):
    description = req.POST.get('r_description')

    res_obj = Research()

    res_obj.r_description = description

    res_obj.save()

    return redirect('res_admin')

def a_res(req):
    return render(req,'a_research.html')

def a_resInsert(req):
    title = req.POST.get('a_res_title')
    description = req.POST.get('a_res_description')
    duration = req.POST.get('a_res_duration'),

    a_res_obj = AResearch()

    a_res_obj.a_res_title = title
    a_res_obj.a_res_description = description
    a_res_obj.a_res_duration = duration

    a_res_obj.save()

    return redirect('a_res_admin')
    
def ff(req):
    return render(req,'ff.html')

def ffInsert(req):
    description = req.POST.get('ff_description')

    ff_obj = Fun()

    ff_obj.ff_description = description

    ff_obj.save()

    return redirect('ff_admin')

def af(req):
    return render(req,'a_fact.html')

def afInsert(req):
    number = req.POST.get('f_number')
    lineone  = req.POST.get('f_lno')
    linetwo = req.POST.get('f_lnt')

    af_obj = AFact()

    af_obj.f_number = number
    af_obj.f_lno = lineone
    af_obj.f_lnt = linetwo

    af_obj.save()

    return redirect('af_admin')

def s(req):
    return render(req,'skill.html')

def sInsert(req):
    description = req.POST.get('s_description')

    s_obj = Skill()

    s_obj.s_description = description

    s_obj.save()

    return redirect('s_admin')

def a_s(req):
    return render(req,'a_skill.html')

def a_sInsert(req):
    percentage = req.POST.get('a_s_perc')
    title = req.POST.get('a_s_title')

    a_s_obj = ASkill()
    
    a_s_obj.a_s_perc = percentage
    a_s_obj.a_s_title = title

    a_s_obj.save()

    return redirect('a_s_admin')

def t_description(req):
    return render(req,'testimonial.html')

def t_descriptionInsert(req):
    description = req.POST.get('t_description')

    t_description_obj = Testimonial()

    t_description_obj.t_description = description

    t_description_obj.save()

    return redirect('t_description_admin')

def f(req):
    return render(req,'feedback.html')

def fInsert(req):
    name = req.POST.get('f_name')
    designation = req.POST.get('f_designation')
    company = req.POST.get('f_company')
    feedback = req.POST.get('f_feed')

    f_obj = Feedback()

    f_obj.f_name = name
    f_obj.f_designation = designation
    f_obj.f_company = company
    f_obj.f_feed = feedback

    f_obj.save()

    return redirect('f_admin')

def srvc_t(req):
    return render(req,'service_t.html')

def srvc_tInsert(req):
    description = req.POST.get('srvc_t')

    srvc_t_obj = Service()

    srvc_t_obj.srvc_t = description

    srvc_t_obj.save()

    return redirect('srvc_t_admin')

def srvc(req):
    return render(req,'service.html')

def srvcInsert(req):
    title = req.POST.get('s_title')
    description = req.POST.get('s_description')

    srvc_obj = Services()

    srvc_obj.s_title = title
    srvc_obj.s_description = description

    srvc_obj.save()

    return redirect('srvc_admin')

def cntc_t(req):
    return render(req,'contact_t.html')

def cntc_tInsert(req):
    title = req.POST.get('cntc_t')

    cntc_t_obj = Contact()

    cntc_t_obj.cntc_t = title

    cntc_t_obj.save()

    return redirect('cntc_t_admin')

def cntc(req):
    return render (req,'contacts.html')

def cntcInsert(req):
    address = req.POST.get('cntc_address')
    number = req.POST.get('cntc_number')
    email = req.POST.get('cntc_email')

    cntc_obj = Contacts()

    cntc_obj.cntc_address = address
    cntc_obj.cntc_number = number
    cntc_obj.cntc_email = email

    cntc_obj.save()

    return redirect('cntc_admin')

