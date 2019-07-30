from django.core.validators import RegexValidator
from django.db import models


# Create your models here.

class Customer(models.Model):
    # alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    # name = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=150)
    confirmpassword = models.CharField(max_length=150)

    def __str__(self):
        return self.firstname

class Bt(models.Model):
    # alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    # name = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    username = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    fnames = models.CharField(max_length=150, null=True)
    lnames = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=150, null=True)
    passwords = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.username

class Company(models.Model):
    adminfirstname = models.CharField(max_length=150, null=True)
    adminlastname = models.CharField(max_length=150, null=True)
    companyname = models.CharField(max_length=150, null=True)
    companyemail = models.CharField(max_length=150, null=True)
    companypassword = models.CharField(max_length=150, null=True)
    companyconfirmpassword = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.adminfirstname

class Station(models.Model):
    companyid = models.ForeignKey(Company, on_delete=models.CASCADE, primary_key=Company.id)
    stationname = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.stationname

class Route(models.Model):
    busno = models.CharField(max_length=150,null=True)
    # Time = models.CharField(max_length=150,null=True)
    # price = models.FloatField(max_length=8,null=True)

    def __str__(self):
        return self.busno

class BusDetail(models.Model):
    busno = models.CharField(max_length=150, null=True)
    Type = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.Type

class xt(models.Model):
    x_time=models.DateTimeField(null=True)
    x_name=models.CharField(max_length=150,null=True)