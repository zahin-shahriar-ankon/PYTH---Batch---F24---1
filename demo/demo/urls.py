"""
URL configuration for demo project.

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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('intro/', views.intro, name = 'intro_admin'),
    path('intro/insert', views.introInsert, name = 'intro_insert'),
    path('works/', views.works, name = 'works_admin'),
    path('works/insert', views.worksInsert, name = 'works_insert'),
    path('about_me/', views.about_me, name = 'about_me_admin'),
    path('about_me/insert', views.about_meInsert, name = 'about_me_insert'),
    path('edu/', views.edu, name = 'edu_admin'),
    path('edu/insert', views.eduInsert, name = 'edu_insert'),
    path('deg/', views.deg, name = 'deg_admin'),
    path('deg/insert', views.degInsert, name = 'deg_insert'),
    path('project/', views.project, name = 'project_admin'),
    path('project/insert', views.projectInsert, name = 'project_insert'),
    path('a_project/', views.a_project, name = 'a_project_admin'),
    path('a_project/insert', views.a_projectInsert, name = 'a_project_insert'),
    path('ex/', views.ex, name = 'ex_admin'),
    path('ex/insert', views.exInsert, name = 'ex_insert'),
    path('a_ex/', views.a_ex, name = 'a_ex_admin'),
    path('a_ex/insert', views.a_exInsert, name = 'a_ex_insert'),
    path('res/', views.res, name = 'res_admin'),
    path('res/insert', views.resInsert, name = 'res_insert'),
    path('a_res/', views.a_res, name = 'a_res_admin'),
    path('a_res/insert', views.a_resInsert, name = 'a_res_insert'),
    path('ff/', views.ff, name = 'ff_admin'),
    path('ff/insert', views.ffInsert, name = 'ff_insert'),
    path('af/', views.af, name = 'af_admin'),
    path('af/insert', views.afInsert, name = 'af_insert'),
    path('s/', views.s, name = 's_admin'),
    path('s/insert', views.sInsert, name = 's_insert'),
    path('a_s/', views.a_s, name = 'a_s_admin'),
    path('a_s/insert', views.a_sInsert, name = 'a_s_insert'),
    path('t_description/', views.t_description, name = 't_description_admin'),
    path('t_description/insert', views.t_descriptionInsert, name = 't_description_insert'),
    path('f/', views.f, name = 'f_admin'),
    path('f/insert', views.fInsert, name = 'f_insert'),
    path('srvc_t/', views.srvc_t, name = 'srvc_t_admin'),
    path('srvc_t/insert', views.srvc_tInsert, name = 'srvc_t_insert'),
    path('srvc/', views.srvc, name = 'srvc_admin'),
    path('srvc/insert', views.srvcInsert, name = 'srvc_insert'),
    path('cntc_t/', views.cntc_t, name = 'cntc_t_admin'),
    path('cntc_t/insert', views.cntc_tInsert, name = 'cntc_t_insert'),
    path('cntc/', views.cntc, name = 'cntc_admin'),
    path('cntc/insert', views.cntcInsert, name = 'cntc_insert'),
]+ static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
