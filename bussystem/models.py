from django.core.validators import RegexValidator
from django.db import models
# from django.db import models
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class Company(models.Model):
    # com_id = models.AutoField(primary_key=True, unique=True)
    adminfirstname = models.CharField(max_length=150, null=True)
    adminlastname = models.CharField(max_length=150, null=True)
    companyname = models.CharField(max_length=150, null=True, unique=True)
    companyemail = models.CharField(max_length=150, null=True, unique=True)
    companypassword = models.CharField(max_length=150, null=True)
    companyconfirmpassword = models.CharField(max_length=150, null=True)

    def __str__(self):

        if self.companyname == None:
            temp = "Company no: "+str(id)
            return temp
        return self.companyname


class Customer(models.Model):
    # alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    # name = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    # cus_foreign = models.ForeignKey(Company, on_delete=models.CASCADE)
    cus_id = models.AutoField(primary_key=True)
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
    # bt_for = models.ForeignKey(Company, on_delete=models.CASCADE)
    # id = models.AutoField(primary_key=True)
    companyidd = models.ForeignKey(Company, on_delete=models.CASCADE)
    bt_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    fnames = models.CharField(max_length=150, null=True)
    lnames = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=150, null=True)
    passwords = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.email

class Station(models.Model):
    companyid = models.ForeignKey(Company, on_delete=models.CASCADE)
    stationname = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.stationname

class BusDetail(models.Model):
    bsid = models.ForeignKey(Company, on_delete=models.CASCADE)
    busno = models.CharField(max_length=150, null=False)
    busplatenumber = models.CharField(max_length=150, null=False)
    # Type = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.busno


class routee(models.Model):
    to_route = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='but_to_fore', null=False, blank=False)
    from_route = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='bus_froom_fore', null=False, blank=False)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, null=False, blank=False)
    bus_details = models.ForeignKey(BusDetail, on_delete=models.CASCADE, null=False, blank=False)
    bus_no = models.CharField(max_length=150, null=False)
    Time = models.CharField(max_length=150, null=True)
    price = models.FloatField(max_length=8, null=True)

    def __str__(self):
        if self.bus_no == None:
            return "ERROR-Busno IS NULL"
        return self.bus_no


class xt(models.Model):
    x_time=models.DateTimeField(null=True)
    x_name=models.CharField(max_length=150,null=True)