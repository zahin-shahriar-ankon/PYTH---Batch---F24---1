from django.db import models

class Intro(models.Model):
    i_name = models.CharField(max_length = 500)
    i_occupation = models.CharField(max_length = 500)

class Works(models.Model):
    w_title = models.CharField(max_length = 500)
    w_description = models.CharField(max_length = 500)

class AboutMe(models.Model):
    a_description = models.CharField(max_length = 500)
    a_name = models.CharField(max_length = 500)
    a_age = models.CharField(max_length = 500)
    a_occupation = models.CharField(max_length = 500)
    a_phone = models.CharField(max_length = 500)
    a_email = models.CharField(max_length = 500)
    a_nationality = models.CharField(max_length = 500)

class Education(models.Model):
    e_description = models.CharField(max_length = 500)

class Degrees(models.Model):
    d_title = models.CharField(max_length = 500)
    d_institution = models.CharField(max_length = 500)
    d_duration = models.CharField(max_length = 500)
    d_description = models.CharField(max_length = 500)

class Project(models.Model):
    p_description = models.CharField(max_length = 500)

class AProject(models.Model):
    ap_description = models.CharField(max_length = 500)

class Experience(models.Model):
    ex_description = models.CharField(max_length = 500)

class AExperience(models.Model):
    a_ex_title = models.CharField(max_length = 500)
    a_ex_institution = models.CharField(max_length = 500)
    a_ex_duration = models.CharField(max_length = 500)
    a_ex_description = models.CharField(max_length = 500)

class Research(models.Model):
    r_description = models.CharField(max_length = 500)

class AResearch(models.Model):
    a_res_title = models.CharField(max_length = 500)
    a_res_description = models.CharField(max_length = 500)
    a_res_duration = models.CharField(max_length = 500)

class Fun(models.Model):
    ff_description = models.CharField(max_length = 500)

class AFact(models.Model):
    f_number = models.CharField(max_length = 500)
    f_lno = models.CharField(max_length = 500)
    f_lnt = models.CharField(max_length = 500)

class Skill(models.Model):
    s_description = models.CharField(max_length = 500)

class ASkill(models.Model):
    a_s_perc = models.CharField(max_length = 500)
    a_s_title = models.CharField(max_length = 500)

class Testimonial(models.Model):
    t_description = models.CharField(max_length = 500)

class Feedback(models.Model):
    f_name = models.CharField(max_length = 500)
    f_designation = models.CharField(max_length = 500)
    f_company = models.CharField(max_length = 500)
    f_feed = models.CharField(max_length = 500)

class Service(models.Model):
    srvc_t = models.CharField(max_length = 500)

class Services(models.Model):
    s_title = models.CharField(max_length = 500)
    s_description = models.CharField(max_length = 500)

class Contact(models.Model):
    cntc_t = models.CharField(max_length = 500)

class Contacts(models.Model):
    cntc_address = models.CharField(max_length = 500)
    cntc_number = models.CharField(max_length = 500)
    cntc_email = models.CharField(max_l