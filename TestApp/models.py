from django.db import models

# Create your models here.
class student(models.Model):
    studentname = models.TextField(blank=True,null=True)
    standard = models.TextField(blank=True,null=True)
    section = models.TextField(blank=True,null=True)
    grade = models.TextField(blank=True,null=True)
     