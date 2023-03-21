from django.db import models
from django.urls import reverse

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.name)


class Course(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)


    def __str__(self):
        return '{}'.format(self.name)

class Requirements(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.CharField(max_length=15)
    gender = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    purpose = models.CharField(max_length=250)
    material = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)
