from django.db import models

class Signup(models.Model):
    fullName= models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=30, blank=True) 

class Login(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30, blank=True) 

class Contact(models.Model):
    name=models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=100)

class Book(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    car = models.CharField(max_length=20)
    pickup_date =  models.DateField()
    return_date =  models.DateField()
