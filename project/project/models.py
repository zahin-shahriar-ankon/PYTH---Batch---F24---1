from django.db import models 

class AboutMe(models.Model):
    name = models.CharField(max_length = 100)
    age = models.CharField(max_length = 50)
    occupation = models.CharField(max_length = 500)
    phone = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    nationality = models.CharField(max_length = 500)
    description = models.CharField(max_length = 500)

class Intro(models.Model):
    i_name = models.CharField(max_length = 100)
    i_occupation = models.CharField(max_length = 500)

class Works(models.Model):
    w_name_one = models.CharField(max_length = 100)
    w_description_one = models.CharField(max_length = 500)
    w_name_one = models.CharField(max_length = 100)
    w_description_one = models.CharField(max_length = 500)
    w_name_one = models.CharField(max_length = 100)
    w_description_one = models.CharField(max_length = 500)
    w_name_one = models.CharField(max_length = 100)
    w_description_one = models.CharField(max_length = 500)
    