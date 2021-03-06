from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.db import IntegrityError
# Create your views here.
from bussystem.models import Customer, Bt, Company, Station, Route
from fontawesome_5.fields import IconField
from datetime import datetime


def deletebt(request):
    bts = Bt.objects.all()
    context = {
        'bts': bts
    }
    return render(request, 'deletebt.html', context)

def delete(request, id):
    bt = Bt.objects.get(pk=id)
    bt.delete()
    return redirect('/deletebt')

# def deletebt(request):
#     return render(request, 'deletebt.html')

def create(request):
    print(request.POST)
    firstname = request.GET['firstname']
    lastname = request.GET['lastname']
    email = request.GET['email']
    password = request.GET['password']
    confirmpassword = request.GET['confirmpassword']

    book_details = Customer(firstname=firstname, lastname=lastname, email=email, password=password,
                            confirmpassword=confirmpassword)
    book_details.save()
    return redirect('/')


def authentication(request):
    print(request.POST)
    if request.session.get('email'):
        messages.success(request, 'You are  Already Loged In')
        return render(request, 'login.html')
    #  return HttpResponse('You are already loged in')

    email = request.GET['email']
    password = request.GET['password']

    customers = Customer.objects.filter(email=email, password=password).count()

    email = request.GET['email']
    passwords = request.GET['password']
    request.POST._mutable = True
    # request.data['customer'] = customer
    bt = Bt.objects.filter(email=email, passwords=passwords).count()

    companyemail = request.GET['email']
    companypassword = request.GET['password']
    request.POST._mutable = True
    # request.data['customer'] = customer
    com = Company.objects.filter(companyemail=companyemail, companypassword=companypassword).count()

    if (customers > 0):
        request.session['email'] = email
        # request.session['password']=Cust_password
        return render(request, 'userticket.html')
    elif (bt > 0):
        request.session['email'] = email
        # request.session['password']=Cust_password
        return render(request, 'BtTicket.html')
    elif (com > 0):
        request.session['email'] = email
        # request.session['password']=Cust_password
        return render(request, 'adminprofile.html')
    else:
        messages.error(request, 'Email Or Password Doesnot match')
        return render(request, 'login.html')
        # return HttpResponse('Email and password doesnt match')

    return render(request, 'login.html')


def signout(request):
    try:
        del request.session['email']
        del request.session['password']
        print('logout')
    except:
        pass
    print('LOL')
    return redirect('/')


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def registrationforuser(request):
    return render(request, 'registrationforuser.html')


def companyregister(request):
    print(request.POST)
    adminfirstname = request.GET.get('adminfirstname')
    adminlastname = request.GET.get('adminlastname')
    companyname = request.GET.get('companyname')
    companyemail = request.GET.get('companyemail')
    companypassword = request.GET.get('companypassword')
    companyconfirmpassword = request.GET.get('companyconfirmpassword')
    company_details = Company(adminfirstname=adminfirstname, adminlastname=adminlastname, companyname=companyname,
                              companyemail=companyemail, companypassword=companypassword,
                              companyconfirmpassword=companyconfirmpassword)
    company_details.save()
    messages.success(request, 'You are  Already Loged In')
    return render(request, 'companyregister.html')



def btticket(request):
    return render(request, 'btticket.html')


def btcancel(request):
    return render(request, 'btcancel.html')


def usercancel(request):
    return render(request, 'usercancel.html')


def userticket(request):
    return render(request, 'userticket.html')


def station(request):
    print(request.POST)
    stationname = request.GET.get('stationname')
    station_details = Station(stationname=stationname)
    station_details.save()
    return render(request, 'AddThings.html')


def routes(request):
    print(request.POST)
    myDate = datetime.now()
    busno = request.GET.get('busno')
    Time = request.GET.get('Time')
    price = request.GET.get('price')
    routes_details= Route(busno=busno, Time=Time, price= price)
    routes_details.save()
    return render(request, 'AddThings.html', {
        'myDate': myDate
    })


def createbt(request):
    print(request.POST)
    username = request.GET.get('username')
    email = request.GET.get('email')
    fnames = request.GET.get('fnames')
    lnames = request.GET.get('lnames')
    address = request.GET.get('address')
    city = request.GET.get('city')
    passwords = request.GET.get('passwords')

    bt_details = Bt(username=username, email=email, fnames=fnames, lnames=lnames, address=address,
                    city=city, passwords=passwords)
    bt_details.save()
    return render(request, 'createbt.html')
    # return redirect('/')



def adminprofile(request):
    return render(request, 'adminprofile.html')


def performance(request):
    return render(request, 'performance.html')


def addthings(request):
    # print(request.POST)
    # fnames = request.GET.get('fnames')
    # lnames = request.GET.get('lnames')
    # bus_details = Bt(busno=username, Type=email, fnames=fnames, lnames=lnames, address=address,
    #                 city=city, passwords=passwords)
    # bus_details.save()
    return render(request, 'addthings.html')


def adminsearch(request):
    return render(request, 'adminsearch.html')
