"""
URL configuration for one project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('intro/', views.intro, name = 'intro_admin'),
    path('intro/insert', views.introInsert, name = 'intro_insert'),
    path('d_box/', views.d_box, name = 'd_box_admin'),
    path('d_box/insert', views.d_boxInsert, name = 'd_box_insert'),
    path('s_work/', views.s_work, name = 's_work_admin'),
    path('s_work/insert', views.s_workInsert, name = 's_work_insert'),
    path('collab/', views.collab, name = 'collab_admin'),
    path('collab/insert', views.collabInsert, name = 'collab_insert'),
    path('tech/', views.tech, name = 'tech_admin'),
    path('tech/insert', views.techInsert, name = 'tech_insert'),#first ss upto this
    path('about_me/', views.about_me, name = 'about_me_admin'),
    path('about_me/insert', views.about_meInsert, name = 'about_me_insert'),
    path('edu_desc/', views.edu_desc, name = 'edu_desc_admin'),
    path('edu_desc/insert', views.edu_descInsert, name = 'edu_desc_insert'),
    path('f_degree/', views.f_degree, name = 'f_degree_admin'),
    path('f_degree/insert', views.f_degreeInsert, name = 'f_degree_insert'),
    path('f_dr/', views.f_dr, name = 'f_dr_admin'),
    path('f_dr/insert', views.f_drInsert, name = 'f_dr_insert'),
    path('sc_degree/', views.sc_degree, name = 'sc_degree_admin'),
    path('sc_degree/insert', views.sc_degreeInsert, name = 'sc_degree_insert'),
    path('sc_dr/', views.sc_dr, name = 'sc_dr_admin'),
    path('sc_dr/insert', views.sc_drInsert, name = 'sc_dr_insert'),
    path('thd_degree/', views.thd_degree, name = 'thd_degree_admin'),
    path('thd_degree/insert', views.thd_degreeInsert, name = 'thd_degree_insert'),
    path('thd_dr/', views.thd_dr, name = 'thd_dr_admin'),
    path('thd_dr/insert', views.thd_drInsert, name = 'thd_dr_insert'),
    path('pjct/', views.pjct, name = 'pjct_admin'),
    path('pjct/insert', views.pjctInsert, name = 'pjct_insert'),
    path('icws/', views.icws, name = 'icws_admin'),
    path('icws/insert', views.icwsInsert, name = 'icws_insert'),
    path('dgvr/', views.dgvr, name = 'dgvr_admin'),
    path('dgvr/insert', views.dgvrInsert, name = 'dgvr_insert'),
    path('doc/', views.doc, name = 'doc_admin'),
    path('doc/insert', views.docInsert, name = 'doc_insert'),
    path('face/', views.face, name = 'face_admin'),
    path('face/insert', views.faceInsert, name = 'face_insert'),
    path('lp/', views.lp, name = 'lp_admin'),
    path('lp/insert', views.lpInsert, name = 'lp_insert'),
    path('ug/', views.ug, name = 'ug_admin'),
    path('ug/insert', views.ugInsert, name = 'ug_insert'),
    path('m_e/', views.m_e, name = 'm_e_admin'),# second ss
    path('m_e/insert', views.m_eInsert, name = 'm_e_insert'),
    path('f_ex/', views.f_ex, name = 'f_ex_admin'),
    path('f_ex/insert', views.f_exInsert, name = 'f_ex_insert'),
    path('f_ex_dr/', views.f_ex_dr, name = 'f_ex_dr_admin'),
    path('f_ex_dr/insert', views.f_ex_drInsert, name = 'f_ex_dr_insert'),
    path('pm/', views.pm, name = 'pm_admin'),
    path('pm/insert', views.pmInsert, name = 'pm_insert'),
    path('pm_dr/', views.pm_dr, name = 'pm_dr_admin'),
    path('pm_dr/insert', views.pm_drInsert, name = 'pm_dr_insert'),
    path('sd/', views.sd, name = 'sd_admin'),
    path('sd/insert', views.sdInsert, name = 'sd_insert'),
    path('sd_dr/', views.sd_dr, name = 'sd_dr_admin'),
    path('sd_dr/insert', views.sd_drInsert, name = 'sd_dr_insert'),
    path('rp/', views.rp, name = 'rp_admin'),
    path('rp/insert', views.rpInsert, name = 'rp_insert'),
    path('f_rch/', views.f_rch, name = 'f_rch_admin'),
    path('f_rch/insert', views.f_rchInsert, name = 'f_rch_insert'),
    path('f_rch_dr/', views.f_rch_dr, name = 'f_rch_dr_admin'),
    path('f_rch_dr/insert', views.f_rch_drInsert, name = 'f_rch_dr_insert'),
    path('s_rch/', views.s_rch, name = 's_rch_admin'),
    path('s_rch/insert', views.s_rchInsert, name = 's_rch_insert'),
    path('s_rch_dr/', views.s_rch_dr, name = 's_rch_dr_admin'),
    path('s_rch_dr/insert', views.s_rch_drInsert, name = 's_rch_dr_insert'),
    path('thd_rch/', views.thd_rch, name = 'thd_rch_admin'),
    path('thd_rch/insert', views.thd_rchInsert, name = 'thd_rch_insert'),
    path('thd_rch_dr/', views.thd_rch_dr, name = 'thd_rch_dr_admin'),
    path('thd_rch_dr/insert', views.thd_rch_drInsert, name = 'thd_rch_dr_insert'),
    path('frt_rch/', views.frt_rch, name = 'frt_rch_admin'),
    path('frt_rch/insert', views.frt_rchInsert, name = 'frt_rch_insert'),
    path('frt_rch_dr/', views.frt_rch_dr, name = 'frt_rch_dr_admin'),
    path('frt_rch_dr/insert', views.frt_rch_drInsert, name = 'frt_rch_dr_insert'),# third ss
    path('fft_rch/', views.fft_rch, name = 'fft_rch_admin'),
    path('fft_rch/insert', views.fft_rchInsert, name = 'fft_rch_insert'),
    path('sxth_rch/', views.sxth_rch, name = 'sxth_rch_admin'),
    path('sxth_rch/insert', views.sxth_rchInsert, name = 'sxth_rch_insert'),
    path('f_fct/', views.f_fct, name = 'f_fct_admin'),
    path('f_fct/insert', views.f_fctInsert, name = 'f_fct_insert'),
    path('f_fn_fct/', views.f_fn_fct, name = 'f_fn_fct_admin'),
    path('f_fn_fct/insert', views.f_fn_fctInsert, name = 'f_fn_fct_insert'),
    path('s_fn_fct/', views.s_fn_fct, name = 's_fn_fct_admin'),
    path('s_fn_fct/insert', views.s_fn_fctInsert, name = 's_fn_fct_insert'),
    path('thd_fn_fct/', views.thd_fn_fct, name = 'thd_fn_fct_admin'),
    path('thd_fn_fct/insert', views.thd_fn_fctInsert, name = 'thd_fn_fct_insert'),
    path('frt_fn_fct/', views.frt_fn_fct, name = 'frt_fn_fct_admin'),
    path('frt_fn_fct/insert', views.frt_fn_fctInsert, name = 'frt_fn_fct_insert'),
 ]
 


