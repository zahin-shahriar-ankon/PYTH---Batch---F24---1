from django.db import models

class AboutMe(models.Model):
    a_name = models.CharField(max_length = 100)
    a_age = models.CharField(max_length = 50)
    a_occupation = models.CharField(max_length = 100)
    a_phone = models.CharField(max_length = 50)
    a_email = models.CharField(max_length = 50)
    a_nationality = models.CharField(max_length = 100)
    a_description = models.CharField(max_length = 500)

class Intro(models.Model):
    i_name = models.CharField(max_length = 100)
    i_occupation = models.CharField(max_length = 100)

class DBox(models.Model):
    d_title = models.CharField(max_length = 100)
    d_description = models.CharField(max_length = 100)

class SWork(models.Model):
    s_w_title = models.CharField(max_length = 100)
    s_w_description = models.CharField(max_length = 100)

class Collab(models.Model):
    c_title = models.CharField(max_length = 100)
    c_description = models.CharField(max_length = 100)

class Tech(models.Model):
    t_title = models.CharField(max_length = 100)
    t_description = models.CharField(max_length = 100)

class EduD(models.Model):
    e_description = models.CharField(max_length = 100)

class FDeg(models.Model):
    f_title = models.CharField(max_length = 100)
    f_institute = models.CharField(max_length = 100)
    f_description = models.CharField(max_length = 100)

class ScDeg(models.Model):
    sc_title = models.CharField(max_length = 100)
    sc_institute = models.CharField(max_length = 100)
    sc_description = models.CharField(max_length = 100)

class ThdDeg(models.Model):
    thd_title = models.CharField(max_length = 100)
    thd_institute = models.CharField(max_length = 100)
    thd_description = models.CharField(max_length = 100)

class Pjct(models.Model):
    pjct_description = models.CharField(max_length = 100)

class Icws(models.Model):
    icws_description = models.CharField(max_length = 100)

class Dgvr(models.Model):
    dgvr_description = models.CharField(max_length = 100)

class Doc(models.Model):
    doc_description = models.CharField(max_length = 100)

class Face(models.Model):
    face_description = models.CharField(max_length = 100)

class Lappy(models.Model):
    lp_description = models.CharField(max_length = 100)

class Ug(models.Model):
    ug_description = models.CharField(max_length = 100)

class M_e(models.Model):
    m_e_description = models.CharField(max_length = 100)

class F_ex(models.Model):
    f_ex_title = models.CharField(max_length = 100)
    f_ex_institute = models.CharField(max_length = 100)
    f_ex_description = models.CharField(max_length = 100)

class Pm(models.Model):
    pm_title = models.CharField(max_length = 100)
    pm_institute = models.CharField(max_length = 100)
    pm_description = models.CharField(max_length = 100)

class Sd(models.Model):
    sd_title = models.CharField(max_length = 100)
    sd_institute = models.CharField(max_length = 100)
    sd_description = models.CharField(max_length = 100)

class Rp(models.Model):
    rp_description = models.CharField(max_length = 100)

class F_rch(models.Model):
    f_rch_title = models.CharField(max_length = 100)
    f_rch_description = models.CharField(max_length = 100)

class S_rch(models.Model):
    s_rch_title = models.CharField(max_length = 100)
    s_rch_description = models.CharField(max_length = 100)

class Thd_rch(models.Model):
    thd_rch_title = models.CharField(max_length = 100)
    thd_rch_description = models.CharField(max_length = 100)

class Frt_rch(models.Model):
    frt_rch_title = models.CharField(max_length = 100)
    frt_rch_description = models.CharField(max_length = 100)

class Frt_rch_dr(models.Model):
    frt_rch_dr = models.CharField(max_length = 100)

class Thd_rch_dr(models.Model):
    thd_rch_dr = models.CharField(max_length = 100)

class S_rch_dr(models.Model):
    s_rch_dr = models.CharField(max_length = 100)

class F_rch_dr(models.Model):
    f_rch_dr = models.CharField(max_length = 100)

class F_ex_dr(models.Model):
    f_ex_dr = models.CharField(max_length = 100)

class Pm_dr(models.Model):
    pm_duration = models.CharField(max_length = 100)

class Sd_dr(models.Model):
    sd_duration = models.CharField(max_length = 100)

class F_dr(models.Model):
    f_duration = models.CharField(max_length = 100)

class Sc_dr(models.Model):
    sc_duration = models.CharField(max_length = 100)

class Thd_dr(models.Model):
    thd_duration = models.CharField(max_length = 100)
    
class Fft_rch(models.Model):
    fft_rch_title = models.CharField(max_length = 100)
    fft_rch_duration = models.CharField(max_length = 100)
    fft_rch_description = models.CharField(max_length = 100)

class Sxth_rch(models.Model):
    sxth_rch_title = models.CharField(max_length = 100)
    sxth_rch_duration = models.CharField(max_length = 100)
    sxth_rch_description = models.CharField(max_length = 100)

class F_fct(models.Model):
    f_fct_description = models.CharField(max_length = 100)

class F_fn_fct(models.Model):
    f_fn_fct_yrs = models.CharField(max_length = 100)
    f_fn_fct_on_description = models.CharField(max_length = 100)
    f_fn_fct_tw_description = models.CharField(max_length = 100)

class S_fn_fct(models.Model):
    s_fn_fct_yrs = models.CharField(max_length = 100)
    s_fn_fct_on_description = models.CharField(max_length = 100)
    s_fn_fct_tw_description = models.CharField(max_length = 100)

class Thd_fn_fct(models.Model):
    thd_fn_fct_yrs = models.CharField(max_length = 100)
    thd_fn_fct_on_description = models.CharField(max_length = 100)
    thd_fn_fct_tw_description = models.CharField(max_length = 100)

class Frt_fn_fct(models.Model):
    frt_fn_fct_yrs = models.CharField(max_length = 100)
    frt_fn_fct_on_description = models.CharField(max_length = 100)
    frt_fn_fct_tw_description = models.CharField(max_length = 100)





