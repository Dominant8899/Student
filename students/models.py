from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    age = models.IntegerField()
    course = models.CharField(max_length=30)
    

