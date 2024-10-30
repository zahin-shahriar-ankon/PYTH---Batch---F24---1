from django.db import models

class AboutMe(models.Model):
    name = models.CharField(max_length = 500)
    age = models.CharField(max_length = 500)
    occupation = models.CharField(max_length = 500)
    phone = models.CharField(max_length = 500)
    email = models.CharField(max_length = 500)
    nationality = models.CharField(max_length = 500)
    description = models.CharField(max_length = 500)

