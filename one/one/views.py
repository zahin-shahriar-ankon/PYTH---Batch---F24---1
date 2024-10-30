from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import *


def home(req):
    intro_data = Intro.objects.get(id = 4)
    about_me_data = AboutMe.objects.get(id = 4)
    d_box_data = DBox.objects.get(id = 3)
    s_work_data = SWork.objects.get(id = 4)
    collab_data = Collab.objects.get(id = 4)
    tech_data = Tech.objects.get(id = 2)
    edu_desc_data = EduD.objects.get(id = 1)
    f_degree_data = FDeg.objects.get(id = 1)
    sc_degree_data = ScDeg.objects.get(id = 1)
    thd_degree_data = ThdDeg.objects.get(id = 1)
    pjct_data = Pjct.objects.get(id = 1)
    icws_data = Icws.objects.get(id = 1)
    dgvr_data = Dgvr.objects.get(id = 1)
    doc_data = Doc.objects.get(id = 1)
    face_data = Face.objects.get(id = 1)
    lappy_data = Lappy.objects.get(id = 1)
    ug_data = Ug.objects.get(id = 1)
    m_e_data = M_e.objects.get(id = 1)
    f_ex_data = F_ex.objects.get(id = 1)
    pm_data = Pm.objects.get(id = 1)
    sd_data = Sd.objects.get(id = 1)
    rp_data = Rp.objects.get(id = 1)
    f_rch_data = F_rch.objects.get(id = 2)
    s_rch_data = S_rch.objects.get(id = 3)
    thd_rch_data = Thd_rch.objects.get(id = 1)
    frt_rch_data = Frt_rch.objects.get(id = 1)# 1st ss
    frt_rch_dr_data = Frt_rch_dr.objects.get(id = 1)
    thd_rch_dr_data = Thd_rch_dr.objects.get(id = 1)
    s_rch_dr_data = S_rch_dr.objects.get(id = 1)
    f_rch_dr_data = F_rch_dr.objects.get(id = 1)
    f_ex_dr_data = F_ex_dr.objects.get(id = 1)
    pm_dr_data = Pm_dr.objects.get(id = 2)
    sd_dr_data = Sd_dr.objects.get(id = 1)
    f_dr_data = F_dr.objects.get(id = 1)
    sc_dr_data = Sc_dr.objects.get(id = 1)
    thd_dr_data = Thd_dr.objects.get(id = 1)
    fft_rch_data = Fft_rch.objects.get(id = 1)
    sxth_rch_data = Sxth_rch.objects.get(id = 1)
    f_fct_data = F_fct.objects.get(id = 2)
    f_fn_fct_data = F_fn_fct.objects.get(id = 1)
    s_fn_fct_data = S_fn_fct.objects.get(id = 1)
    thd_fn_fct_data = Thd_fn_fct.objects.get(id = 1)
    frt_fn_fct_data = Frt_fn_fct.objects.get(id = 1)


   
    data = {'a' : about_me_data, 'i' : intro_data, 'd' : d_box_data, 's' : s_work_data, 'c' : collab_data, 't' : tech_data, 'e' : edu_desc_data, 'f' : f_degree_data, 'sc' : sc_degree_data, 'thd' : thd_degree_data, 'p' : pjct_data, 'icws' : icws_data, 'dgvr' : dgvr_data, 'doc' : doc_data, 'face' : face_data, 'lp' : lappy_data, 'ug' : ug_data, 'm_e' : m_e_data, 'f_ex' : f_ex_data, 'pm' : pm_data, 'sd' : sd_data, 'rp'
    : rp_data, 'f_rch' : f_rch_data, 's_rch' : s_rch_data, 'thd_rch' : thd_rch_data, 'frt_rch' : frt_rch_data,'frt_dr' : frt_rch_dr_data, 't_dr' : thd_rch_dr_data, 's_dr' : s_rch_dr_data, 'f_dr' : f_rch_dr_data, 'f_ex_dr' : f_ex_dr_data, 'pm_dr' : pm_dr_data, 'sd_dr' : sd_dr_data, 'f_dur' : f_dr_data, 'sc_dr' : sc_dr_data, 'thd_dr' : thd_dr_data, 'fft_rch' : fft_rch_data, 'sxth_rch' : sxth_rch_data, 'f_fct' : f_fct_data, 'f_fn_fct' : f_fn_fct_data, 's_fn_fct' : s_fn_fct_data, 'thd_fn_fct' : thd_fn_fct_data, 'frt_fn_fct' : frt_fn_fct_data}

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

def d_box(req):
    return render(req,'d_box.html')

def d_boxInsert(req):
    title = req.POST.get('d_title')
    description = req.POST.get('d_description')

    d_box_obj = DBox()

    d_box_obj.d_title = title
    d_box_obj.d_description = description

    d_box_obj.save()
    
    return redirect('d_box_admin')

def s_work(req):
    return render(req,'s_work.html')

def s_workInsert(req):
    title = req.POST.get('s_w_title')
    description = req.POST.get('s_w_description')

    s_work_obj = SWork()

    s_work_obj.s_w_title = title
    s_work_obj.s_w_description = description

    s_work_obj.save()

    return redirect('s_work_admin')

def collab(req):
    return render(req,'collab.html')

def collabInsert(req):
    title = req.POST.get('c_title')
    description = req.POST.get('c_description')

    collab_obj = Collab()

    collab_obj.c_title = title
    collab_obj.c_description = description

    collab_obj.save()

    return redirect('collab_admin')

def tech(req):
    return render(req,'tech.html')

def techInsert(req):
    title = req.POST.get('t_title')
    description = req.POST.get('t_description')

    tech_obj = Tech()

    tech_obj.t_title = title
    tech_obj.t_description = description

    tech_obj.save()

    return redirect('tech_admin')

def about_me(req):
    return render(req,'about_me.html')

def about_meInsert(req):
    name = req.POST.get('a_name')
    age = req.POST.get('a_age')
    occupation = req.POST.get('a_occupation')
    phone = req.POST.get('a_phone')
    email = req.POST.get('a_email')
    nationality = req.POST.get('a_nationality')
    description = req.POST.get('a_description')

    about_me_obj = AboutMe()

    about_me_obj.a_name = name
    about_me_obj.a_age = age
    about_me_obj.a_occupation = occupation
    about_me_obj.a_phone = phone
    about_me_obj.a_email = email
    about_me_obj.a_nationality = nationality
    about_me_obj.a_description = description

    about_me_obj.save()

    return redirect('about_me_admin')

def edu_desc(req):
    return render(req,'edu_desc.html')

def edu_descInsert(req):
    description = req.POST.get('e_description')

    edu_desc = EduD()

    edu_desc.e_description = description

    edu_desc.save()

    return redirect('edu_desc_admin')

def f_degree(req):
    return render(req,'f_degree.html')

def f_degreeInsert(req):
    title = req.POST.get('f_title')
    institute = req.POST.get('f_institute')
    description = req.POST.get('f_description')

    f_degree_obj = FDeg()

    f_degree_obj.f_title = title
    f_degree_obj.f_institute = institute
    f_degree_obj.f_description = description

    f_degree_obj.save()

    return redirect('f_degree_admin')

def sc_degree(req):
    return render(req,'sc_degree.htm')

def sc_degreeInsert(req):
    title = req.POST.get('sc_title')
    institute = req.POST.get('sc_institute')
    description = req.POST.get('sc_description')

    sc_degree_obj = ScDeg()

    sc_degree_obj.sc_title = title
    sc_degree_obj.sc_institute = institute
    sc_degree_obj.sc_description = description

    sc_degree_obj.save()

    return redirect('sc_degree_admin')
        
def thd_degree(req):
    return render(req,'thd_degree.html')

def thd_degreeInsert(req):
    title = req.POST.get('thd_title')
    institute = req.POST.get('thd_institute')
    description = req.POST.get('thd_description')

    thd_degree_obj = ThdDeg()

    thd_degree_obj.thd_title = title
    thd_degree_obj.thd_institute = institute
    thd_degree_obj.thd_description = description

    thd_degree_obj.save()

    return redirect('thd_degree_admin')
    
def pjct(req):
    return render(req,'pjct.html')

def pjctInsert(req):
    description = req.POST.get('pjct_description')

    pjct_obj = Pjct()

    pjct_obj.pjct_description = description

    pjct_obj.save()

    return redirect('pjct_admin')

def icws(req):
    return render(req,'icws.html')

def icwsInsert(req):
    description = req.POST.get('icws_description')

    icws_obj = Icws()

    icws_obj.icws_description = description

    icws_obj.save()

    return redirect('icws_admin')

def dgvr(req):
    return render(req,'dgvr.html')

def dgvrInsert(req):
    description = req.POST.get('dgvr_description')

    dgvr_obj = Dgvr()

    dgvr_obj.dgvr_description = description

    dgvr_obj.save()

    return redirect('dgvr_admin')

def doc(req):
    return render(req,'doc.html')

def docInsert(req):
    description = req.POST.get('doc_description')

    doc_obj = Doc()

    doc_obj.doc_description = description

    doc_obj.save()

    return redirect('doc_admin')

def face(req):
    return render(req,'face.html')

def faceInsert(req):
    description = req.POST.get('face_description')

    face_obj = Face()

    face_obj.face_description = description

    face_obj.save()

    return redirect('face_admin')
    
def lp(req):
    return render(req,'lappy.html')

def lpInsert(req):
    description = req.POST.get('lp_description')

    lappy_obj = Lappy()

    lappy_obj.lp_description = description

    lappy_obj.save()

    return redirect('lp_admin')

def ug(req):
    return render(req,'ug.html')

def ugInsert(req):
    description =  req.POST.get('ug_description')

    ug_obj = Ug()

    ug_obj.ug_description = description

    ug_obj.save()

    return redirect('ug_admin')

def m_e(req):
    return render(req,'m_e.html')

def m_eInsert(req):
    description = req.POST.get('m_e_description')

    m_e_obj = M_e()

    m_e_obj.m_e_description = description

    m_e_obj.save()

    return redirect('m_e_admin')

def f_ex(req):
    return render(req,'f_ex.html')

def f_exInsert(req):
    title = req.POST.get('f_ex_title')
    institute = req.POST.get('f_ex_institute')
    description = req.POST.get('f_ex_description')

    f_ex_obj = F_ex()

    f_ex_obj.f_ex_title = title
    f_ex_obj.f_ex_institute = institute
    f_ex_obj.f_ex_description = description

    f_ex_obj.save()

    return redirect('f_ex_admin')

def pm(req):
    return render(req,'pm.html')

def pmInsert(req):
    title = req.POST.get('pm_title')
    institute = req.POST.get('pm_institute')
    description = req.POST.get('pm_description')

    pm_obj = Pm()

    pm_obj.pm_title = title
    pm_obj.pm_institute = institute
    pm_obj.pm_description = description

    pm_obj.save()

    return redirect('pm_admin')

def sd(req):
    return render(req,'sd.html')

def sdInsert(req):
    title = req.POST.get('sd_title')
    institute = req.POST.get('sd_institute')
    description = req.POST.get('sd_description')

    sd_obj = Sd()

    sd_obj.sd_title = title
    sd_obj.sd_institute = institute
    sd_obj.sd_description = description

    sd_obj.save()

    return redirect('sd_admin')

def rp(req):
    return render(req,'rp.html')

def rpInsert(req):
    description = req.POST.get('rp_description')

    rp_obj = Rp()

    rp_obj.rp_description = description

    rp_obj.save()

    return redirect('rp_admin')

def f_rch(req):
    return render(req,'f_rch.html')

def f_rchInsert(req):
    title = req.POST.get('f_rch_title')
    description = req.POST.get('f_rch_description')
    
    f_rch_obj = F_rch()

    f_rch_obj.f_rch_title = title
    f_rch_obj.f_rch_description = description

    f_rch_obj.save()

    return redirect('f_rch_admin')

def s_rch(req):
    return render(req,'s_rch.html')

def s_rchInsert(req):
    title = req.POST.get('s_rch_title')
    description = req.POST.get('s_rch_description')

    s_rch_obj = S_rch()

    s_rch_obj.s_rch_title = title
    s_rch_obj.s_rch_description = description

    s_rch_obj.save()

    return redirect('s_rch_admin')

def thd_rch(req):
    return render(req,'thd_rch.html')

def thd_rchInsert(req):
    title = req.POST.get('thd_rch_title')
    description = req.POST.get('thd_rch_description')

    thd_rch_obj = Thd_rch()

    thd_rch_obj.thd_rch_title = title
    thd_rch_obj.thd_rch_description = description

    thd_rch_obj.save()

    return redirect('thd_rch_admin')

def thd_rch_dr(req):
    return render(req,'thd_rch_dr.html')

def thd_rch_drInsert(req):
    duration = req.POST.get('thd_rch_dr')

    thd_rch_dr_obj = Thd_rch_dr()

    thd_rch_dr_obj.thd_rch_dr = duration

    thd_rch_dr_obj.save()

    return redirect('thd_rch_dr_admin')

def frt_rch(req):
    return render(req,'frt_rch.html')

def frt_rchInsert(req):
    title = req.POST.get('frt_rch_title')
    description = req.POST.get('frt_rch_description')

    frt_rch_obj = Frt_rch()

    frt_rch_obj.frt_rch_title = title
    frt_rch_obj.frt_rch_description = description

    frt_rch_obj.save()

    return redirect('frt_rch_admin')

def frt_rch_dr(req):
    return render(req,'frt_rch_dr.html')

def frt_rch_drInsert(req):
    duration = req.POST.get('frt_rch_dr')

    frt_rch_obj = Frt_rch_dr()

    frt_rch_obj.frt_rch_dr = duration

    frt_rch_obj.save()

    return redirect('frt_rch_dr_admin')

def s_rch_dr(req):
    return render(req,'s_rch_dr.html')

def s_rch_drInsert(req):
    duration = req.POST.get('s_rch_dr_title')

    s_rch_dr_obj = S_rch_dr()

    s_rch_dr_obj.s_rch_dr = duration

    s_rch_dr_obj.save()

    return redirect('s_rch_dr_admin')

def f_rch_dr(req):
    return render(req,'f_rch_dr.html')

def f_rch_drInsert(req):
    duration = req.POST.get('f_rch_dr_title')

    f_rch_dr_obj = F_rch_dr()

    f_rch_dr_obj.f_rch_dr = duration

    f_rch_dr_obj.save()

    return redirect('f_rch_dr_admin')

def f_ex_dr(req):
    return render(req,'f_ex_dr.html')

def f_ex_drInsert(req):
    duration = req.POST.get('f_ex_dr')

    f_ex_dr_obj = F_ex_dr()

    f_ex_dr_obj.f_ex_dr = duration

    f_ex_dr_obj.save()

    return redirect('f_ex_dr_admin')

def pm_dr(req):
    return render(req,'pm_dr.html')

def pm_drInsert(req):
    duration = req.POST.get('pm_duration')

    pm_dr_obj = Pm_dr()

    pm_dr_obj.pm_duration = duration

    pm_dr_obj.save()
    
    return redirect('pm_dr_admin')

def sd_dr(req):
    return render(req,'sd_dr.html')

def sd_drInsert(req):
    duration = req.POST.get('sd_duration')

    sd_dr_obj = Sd_dr()

    sd_dr_obj.sd_duration = duration

    sd_dr_obj.save()

    return redirect('sd_dr_admin')

    
def f_dr(req):
    return render(req,'f_dr.html')

def f_drInsert(req):
    duration = req.POST.get('f_duration')

    f_dr_obj = F_dr()

    f_dr_obj.f_duration = duration

    f_dr_obj.save()

    return redirect('f_dr_admin')

def sc_dr(req):
    return render(req,'sc_dr.html')

def sc_drInsert(req):
    duration = req.POST.get('sc_duration')

    sc_d_obj = Sc_dr()

    sc_d_obj.sc_duration = duration

    sc_d_obj.save()

    return redirect('sc_dr_admin')

def thd_dr(req):
    return render(req,'thd_dr.html')

def thd_drInsert(req):
    duration = req.POST.get('thd_duration')

    thd_dr_obj = Thd_dr()

    thd_dr_obj.thd_duration = duration

    thd_dr_obj.save()

    return redirect('thd_dr_admin')


def fft_rch(req):
    return render(req,'fft_rch.html')

def fft_rchInsert(req):
    title = req.POST.get('fft_rch_title')
    duration = req.POST.get('fft_rch_duration')
    description = req.POST.get('fft_rch_description')

    fft_rch_obj = Fft_rch()

    fft_rch_obj.fft_rch_title = title
    fft_rch_obj.fft_rch_duration = duration
    fft_rch_obj.fft_rch_description = description

    fft_rch_obj.save()
    
    return redirect('fft_rch_admin')

def sxth_rch(req):
    return render(req,'sxth.html')

def sxth_rchInsert(req):
    title = req.POST.get('sxth_rch_title')
    description = req.POST.get('sxth_rch_description')
    duration = req.POST.get('sxth_rch_duration')

    sxth_rch_obj = Sxth_rch()

    sxth_rch_obj.sxth_rch_title = title
    sxth_rch_obj.sxth_rch_description = description
    sxth_rch_obj.sxth_rch_duration = duration

    sxth_rch_obj.save()


    return redirect('sxth_rch_admin')

def f_fct(req):
    return render(req,'f_fct.html')

def f_fctInsert(req):
    description = req.POST.get('f_fct_description')

    f_fct_obj = F_fct()

    f_fct_obj.f_fct_description = description

    f_fct_obj.save()

    return redirect('f_fct_admin')


def f_fn_fct(req):
    return render(req,'f_fn_fct.html')

def f_fn_fctInsert(req):
    years = req.POST.get('f_fn_fct_yrs')
    description_one = req.POST.get('f_fn_fct_on_description')
    description_two = req.POST.get('f_fn_fct_tw_description')

    f_fn_fct_obj = F_fn_fct()

    f_fn_fct_obj.f_fn_fct_yrs = years
    f_fn_fct_obj.f_fn_fct_on_description = description_one
    f_fn_fct_obj.f_fn_fct_tw_description = description_two

    f_fn_fct_obj.save()

    return redirect('f_fn_fct_admin')

def s_fn_fct(req):
    return render(req,'s_fn_fct.html')

def s_fn_fctInsert(req):
    years = req.POST.get('s_fn_fct_yrs')
    description_one = req.POST.get('s_fn_fct_on_description')
    description_two = req.POST.get('s_fn_fct_tw_description')

    s_fn_fct_obj = S_fn_fct()

    s_fn_fct_obj.s_fn_fct_yrs = years
    s_fn_fct_obj.s_fn_fct_on_description = description_one
    s_fn_fct_obj.s_fn_fct_tw_description = description_two

    s_fn_fct_obj.save()

    return redirect('s_fn_fct_admin')

def thd_fn_fct(req):
    return render(req,'thd_fn_fct.html')

def thd_fn_fctInsert(req):
    years = req.POST.get('thd_fn_fct_yrs')
    description_one = req.POST.get('thd_fn_fct_on_description')
    description_two = req.POST.get('thd_fn_fct_tw_description')

    thd_fn_fct_obj = Thd_fn_fct()

    thd_fn_fct_obj.thd_fn_fct_yrs = years
    thd_fn_fct_obj.thd_fn_fct_on_description = description_one
    thd_fn_fct_obj.thd_fn_fct_tw_description = description_two

    thd_fn_fct_obj.save()

    return redirect('thd_fn_fct_admin')
    
def frt_fn_fct(req):
    return render(req,'frt_fn_fct.html')

def frt_fn_fctInsert(req):
    years = req.POST.get('frt_fn_fct_yrs')
    description_one = req.POST.get('frt_fn_fct_on_description')
    description_two = req.POST.get('frt_fn_fct_tw_description')

    frt_fn_fct_obj = Frt_fn_fct()

    frt_fn_fct_obj.frt_fn_fct_yrs = years
    frt_fn_fct_obj.frt_fn_fct_on_description = description_one
    frt_fn_fct_obj.frt_fn_fct_tw_description = description_two

    frt_fn_fct_obj.save()

    return redirect('frt_fn_fct_admin')

def ms_desc(req):
    return render(req,'ms_desc.html')

def ms_descInsert(req):
    description = req.POST.get('ms_desc_description')
    return redirect('ms_desc_admin')



