from __future__ import unicode_literals
from django.conf import settings
import json
from pprint import pprint
from django.core.mail import send_mail
import random
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.db import IntegrityError
# Create your views here.
from bussystem.models import *
from fontawesome_5.fields import IconField
from datetime import datetime

from django.views.generic.base import TemplateView
import stripe # new


stripe.api_key = settings.STRIPE_SECRET_KEY # new


# def deletebt(request):
#     return render(request, 'deletebt.html')


def companyregister(request):
    print(request.POST)
    if request.session.get('val_code'):
        del request.session['val_code']
    adminfirstname = request.GET.get('adminfirstname')
    adminlastname = request.GET.get('adminlastname')
    companyname = request.GET.get('companyname')
    companyemail = request.GET.get('mail')
    companypassword = request.GET.get('companypassword')
    companyconfirmpassword = request.GET.get('companyconfirmpassword')

    if (companyconfirmpassword == companypassword):
        admin_name = adminfirstname
        admin_email = companyemail
        validation_code = random.randint(111111, 999999)
        validation_code = str(validation_code)

        # check_verification_code(num)
        mystr = "Hello Mr. " + admin_name + " Your six digit verification code is " + validation_code
        send_mail(
            'Email Verification ',
            mystr,
            settings.EMAIL_HOST_USER,
            [admin_email],
            fail_silently=False,
        )
        thisdict = {
            "adminfirstname": adminfirstname,
            "adminlastname": adminlastname,
            "companyname": companyname,
            "companyemail": companyemail,
            "companypassword": companypassword,
            "companypassword": companypassword,
            "companyconfirmpassword": companyconfirmpassword,
            "validation_code": validation_code,
        }
        r = json.dumps(thisdict)
        loaded_r = json.loads(r)
        print('loaded r =', loaded_r)

        request.session['val_code'] = loaded_r
        if request.session.get('val_code'):
            print("\n\n\n", request.session['val_code'].pop('companyconfirmpassword'))
        return render(request, 'emailvalidationforcomapany.html')

    else:
        messages.error(request, 'Passwords didnt match')
        return redirect('/callcompanyregister')
    # if(companyconfirmpassword == companypassword):
    #

    #     company_details.save()
    #
        # if request.session.get('email'):
        #     del request.session['email']
        #
        # request.session['email'] = companyemail
        # # messages.success(request, 'You are  Already Loged In')
        # return redirect('/adminprofile')
    #
    # else:
    #     messages.success(request, 'Passwords didnt match')
    return render(request, 'companyregister.html')

def validation_code(request):
    try:
        vercode = request.GET['verifycode']

        r = json.dumps(request.session['val_code'])
        loaded_r = json.loads(r)
        print("First name takko na ",loaded_r['validation_code'])
        # print("\nValue in session code ",vercode)
        if str(vercode) == str(loaded_r['validation_code']):
            print("First name ", loaded_r['adminfirstname'])
            # print("Last name ", loaded_r['lastname'])
            # print("Com name ", loaded_r['companyname'])
            print("Mail name ", loaded_r['companyemail'])
            # print("Pass name ", loaded_r['password'])
            # print("CPASS name ", loaded_r['companyconfirmpassword'])
            # book_details = Customer(firstname=str(loaded_r['firstname']), lastname=str(loaded_r['lastname']),
            #                         email=str(loaded_r['email']), password=str(loaded_r['password']),
            #                         confirmpassword=str(loaded_r['password']))
            # book_details.save()
            book_detail = Company(adminfirstname=str(loaded_r['adminfirstname']), adminlastname=str(loaded_r['adminlastname']), companyname=str(loaded_r['companyname']), companyemail=str(loaded_r['companyemail']), companypassword=str(loaded_r['companypassword']), companyconfirmpassword=str(loaded_r['companypassword']))
            book_detail.save()
            if request.session.get('email'):
                del request.session['email']

            request.session['email'] = loaded_r['companyemail']
            # messages.success(request, 'You are  Already Loged In')
            return redirect('/adminprofile')

        return render(request, 'home.html')

    except:
        return HttpResponse('Some exception occured')


def create(request):
    print(request.POST)
    if request.session.get('val_code'):
        del request.session['val_code']
    firstname = request.GET['firstname']
    lastname = request.GET['lastname']
    email = request.GET['email']
    password = request.GET['password']
    confirmpassword = request.GET['confirmpassword']
    if(password == confirmpassword):
        customer_name = firstname
        customer_email = email
        validation_code = random.randint(111111, 999999)
        validation_code = str(validation_code)

    # check_verification_code(num)
        mystr = "Hello Mr. " + customer_name + " Your six digit verification code is " + validation_code
        send_mail(
            'Email Verification ',
            mystr,
            settings.EMAIL_HOST_USER,
            [customer_email],
            fail_silently=False,
        )
        thisdict = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "password":password,
            "confirmpassword":confirmpassword,
            "validation_code":validation_code,
            "confirmpassword": confirmpassword
        }
    # request.session['validation_code'] = validation_code
        r = json.dumps(thisdict)
        loaded_r = json.loads(r)
        print('loaded r =', loaded_r)

        request.session['val_code'] = loaded_r
        if request.session.get('val_code'):
            print("\n\n\n",request.session['val_code'].pop('confirmpassword'))

    # book_details = Customer(firstname=firstname, lastname=lastname, email=email, password=password,
    #                         confirmpassword=confirmpassword)
    # book_details.save()
        return render(request, 'emailvalidationforuser.html')
    else:
        messages.error(request, 'Passwords didnt match')
        return redirect('/registrationforuser')
    return render(request, 'registrationforuser.html')


def validation_code_check(request):
    try:
        vercode = request.GET['verifycode']

        r = json.dumps(request.session['val_code'])
        loaded_r = json.loads(r)
        print("First name takko na ",loaded_r['validation_code'])
        # print("\nValue in session code ",vercode)
        if str(vercode)== str(loaded_r['validation_code']):
            book_details = Customer(firstname=str(loaded_r['firstname']), lastname=str(loaded_r['lastname']), email=str(loaded_r['email']), password=str(loaded_r['password']),
                                    confirmpassword=str(loaded_r['password']))
            book_details.save()
            return redirect('/userticket')

        return render(request, 'home.html')

    except:
        return HttpResponse('Some exception occured')


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
        return redirect('/userticket')
    elif (bt > 0):
        request.session['email'] = email
        # request.session['password']=Cust_password
        return redirect('/btticket')
    elif (com > 0):
        request.session['email'] = companyemail
        # request.session['password']=Cust_password
        return redirect('/adminprofile')
    else:
        messages.error(request, 'Email Or Password Doesnot match')
        return render(request, 'login.html')
        # return HttpResponse('Email and password doesnt match')

    return render(request, 'login.html')


def signout(request):
    try:
        del request.session['email']
        # del request.session['password']
        print('logout')
        return redirect('/signout')
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


def callcompanyregister(request):
    # print(request.POST)
    return render(request, 'companyregister.html')


def buyticketuser(request, id):
    rou = routee.objects.get(pk=id)
    checkedone = '1A'
    checkedtwo = '1C'
    print("NHI")
    all_booked_seats = rou.booked_seats
    all_buy_seats = rou.buy_seats

    if len(all_booked_seats) > 0:
        ary = all_booked_seats.split(',')
    else:
        ary = []

    if len(all_buy_seats) > 0:
        bry = all_buy_seats.split(',')
    else:
        bry = []

    context = {
        'id': id,
        'ary': ary,
        'bry': bry,
        'checkedone': checkedone,
        'checkedtwo': checkedtwo,
    }

    return render(request, 'buyticketuser.html', context)


def buyticketbt(request, id):
    # print(request.POST)
    return render(request, 'b.html')

def btticket(request):

    if request.session.get('email'):

        email = request.session['email']
        btID = Bt.objects.get(email=email)

        x=Company.objects.get(id=btID.companyidd.id)
        stations = Station.objects.filter(companyid=x)

        context = {
            'stations': stations,
        }


        return render(request, 'BtTicket.html', context)

    else:
        return HttpResponse("Bt is not logged in")
def btcancel(request):
    return render(request, 'btcancel.html')


def usercancel(request):
    return render(request, 'usercancel.html')


def userticket(request):
    stations = Station.objects.all()
    x = 43;
    context = {
        'stations': stations,
        'x':x
    }
    return render(request, 'userticket.html', context)


def station(request):
    print(request.POST)
    stationname = request.GET.get('stationname')
    email = request.session['email']

    if request.session.get('email'):
        new_station = Company.objects.get(companyemail=email)

    station_details = Station(companyid=new_station, stationname=stationname)
    station_details.save()
    # sta = Station.objects.all()
    # context = {
    #     'sta': sta
    # }
    return render(request, 'AddThings.html')


def createbt(request):
    print(request.POST)
    username = request.GET.get('username')
    eemail = request.GET.get('email')
    fnames = request.GET.get('fnames')
    lnames = request.GET.get('lnames')
    address = request.GET.get('address')
    city = request.GET.get('city')
    passwords = request.GET.get('passwords')
    email = request.session['email']
    print("Ja rha")
    if request.session.get('email'):
        newbusno = Company.objects.get(companyemail=email)
        print("gia")
    if not (Bt.objects.filter(email=eemail).count()>0 and eemail != ''):
        bt_details = Bt(companyidd= newbusno, username=username, email=eemail, fnames=fnames, lnames=lnames, address=address,
                        city=city, passwords=passwords)
        print("save")
        bt_details.save()
    print("nhi gia")
    return render(request, 'createbt.html')
    # return redirect('/')



def deletebt(request):

    if request.session.get('email'):

        email = request.session['email']
        x = Company.objects.get(companyemail=email)
        bts = Bt.objects.filter(companyidd=x)



        context = {
            'bts': bts
        }
        return render(request, 'deletebt.html', context)

def delete(request, id):
    bt = Bt.objects.get(pk=id)
    bt.delete()
    return redirect('/deletebt')





def adminprofile(request):
    try:
        email = request.session['email']
        if request.session.get('email'):
            newbusno = Company.objects.get(companyemail=email)
            com_username=newbusno.adminfirstname
            com_userlastname=newbusno.adminlastname
            com_name=newbusno.companyname
            companyemail=newbusno.companyemail
            companypassword=newbusno.companypassword
            cusid=newbusno.id
            context = {
                'com_name':com_name,
                'com_username':com_username,
                'com_userlastname':com_userlastname,
                'companyemail':companyemail,
                'companypassword':companypassword,
                'cusid':cusid,
            }
        return render(request, 'adminprofile.html', context)

    except:
        return HttpResponse("There were some problems encountered")

def performance(request):
    return render(request, 'performance.html')


def update(request):
    # email = request.session['email']
    #
    # if request.session.get('email'):
    #     books = Company.objects.get(str(pk=id))
    #     context = {
    #         'books': books
    #     }
    return render(request, 'update.html')


def edit(request, id):
    # books = Company.objects.get(pk=id)
    # books.title = request.GET['title']


    return redirect('/')

def root_selectionn(request):
    # stations = Station.objects.filter(companyid=Company.objects.get(id=2))

    stations = Station.objects.all()
    s1 = request.GET['TeamComp1']
    s2 = request.GET['TeamComp2']

    all_routes = routee.objects.filter(to_route=Station.objects.get(id=s1),from_route=Station.objects.get(id=s2))

    if(all_routes.count()==0):
        print('No route found')
    else:
        for i in all_routes:
            print(i.bus_no)

    context = {
        'all_routes': all_routes,
        'stations':stations,
    }

    return render(request, 'userticket.html', context)


def root_selectionn_for_BT(request):
    # stations = Station.objects.filter(companyid=Company.objects.get(id=2))

    stations = Station.objects.all()
    s1 = request.GET['TeamComp1']
    s2 = request.GET['TeamComp2']

    all_routes = routee.objects.filter(to_route=Station.objects.get(id=s1),from_route=Station.objects.get(id=s2))

    if(all_routes.count()==0):
        print('No route found')
    else:
        for i in all_routes:
            print(i.bus_no)

    context = {
        'all_routes': all_routes,
        'stations':stations,
    }

    return render(request, 'BtTicket.html', context)


def addthings(request):
    busno = request.GET.get('seats')
    busplatenumber = request.GET.get('platenumber')
    email = request.session['email']


    if request.session.get('email'):
        newbusno = Company.objects.get(companyemail=email)
        com_name=newbusno.companyname
        com_id = Company.objects.get(companyemail=email).id
        mystations=Station.objects.filter(companyid=com_id)
        context = {
            'mystations': mystations,
            'com_name':com_name
        }
    routes_details = BusDetail(bsid=newbusno, busno=busno, busplatenumber=busplatenumber)
    routes_details.save()
    return render(request, 'addthings.html',context)


def calladdthings(request):
    try:
        email = request.session['email']
        if request.session.get('email'):
            com_id = Company.objects.get(companyemail=email).id
            x=Company.objects.get(id=com_id)
            mystations=Station.objects.filter(companyid=com_id)
            rou=routee.objects.filter()
            b_details=BusDetail.objects.filter(bsid=x)

            context = {
                'mystations': mystations,
                'rou':rou,
                'b_details':b_details,
            }
            return render(request, 'addthings.html',context)
        else:
            return HttpResponse("You need to signin for this page")

    except:
        return HttpResponse("There were some problems encountered")

# def testArray(request):
#     try:
#         ary = ["1A","2B","3C"]
#         context = {
#             'ary': ary,
#         }
#         return render(request, 'bookticket.html', context)
#     except:
#         return HttpResponse("There were some problems encountered")

def routes(request):
    print(request.POST)
    busno= request.GET.get('busno')
    Time = request.GET.get('Time')
    price = request.GET.get('price')
    dep = request.GET.get('dep')
    arrive = request.GET.get('arrive')
    email = request.session['email']
    temp=BusDetail.objects.get(id=busno).busno

    if request.session.get('email'):
        newbus = Company.objects.get(companyemail=email)


    routes_details= routee(company_name=newbus,bus_details=BusDetail.objects.get(id=busno) ,bus_no=temp, Time=Time, price= price, to_route= Station.objects.get(id=dep), from_route=Station.objects.get(id=arrive))
    routes_details.save()
    return render(request, 'AddThings.html')


def adminsearch(request):
    email = request.session['email']
    if request.session.get('email'):
        # com_id = Company.objects.get(companyemail=email).id
        # mstation = Station.objects.filter(companyid=com_id)
        # rou = routee.objects.filter()
        com_id = Company.objects.get(companyemail=email).id
        mstation = Station.objects.filter(companyid=com_id)
        context = {
            'mystations': mstation,
        }
    return render(request, 'adminsearch.html', context)


def bookticket(request, id):
    rou = routee.objects.get(pk=id)
    checkedone = '1A'
    checkedtwo = '1C'
    print("NHI")
    all_booked_seats = rou.booked_seats
    all_buy_seats = rou.buy_seats

    if len(all_booked_seats)>0:
        ary = all_booked_seats.split(',')
    else:
        ary=[]

    if len(all_buy_seats)>0:
        bry = all_buy_seats.split(',')
    else:
        bry=[]


    print(ary)
    context = {
        'id':id,
        'ary': ary,
        'bry': bry,
        'checkedone': checkedone,
        'checkedtwo' : checkedtwo,
    }

    return render(request, 'bookticket.html', context)


def ticket_done(request, id):
    # bt = Bt.objects.get(pk=id)
    # bt.delete()
    temp_str = ""
    username= request.GET.get('username')
    phone = request.GET.get('phone')
    cnic = request.GET.get('cnic')
    email= request.GET.get('email')
    # amount = request.GET.get('amount')
    seatsno = request.GET.get('seatsno')
    noofseats = request.GET.getlist('checks[]')
    print('\nSeat booked are ',noofseats)
    # total_amount = noofseats.count()
    total_amount=0
    for i in noofseats:
        temp_str=temp_str+str(i)+","
        total_amount=total_amount+1
    temp_str = temp_str[:-1]

    noofseats=str(temp_str)
    print(noofseats)
    print(username)
    print('Temppppp')
    rou=routee.objects.get(pk=id)
    total_amount=total_amount*rou.price


    # check_verification_code(num)
    mystr = "Hello your ticket has been booked successfully " + "\nEmail: "+ email +"\nName: " + username + "\nPhone: " + phone + "\nCNIC: "+ cnic + "\nSeats booked are: "+ temp_str + "\nPrice: " + str(total_amount)
    send_mail(
        'Ticket confirmation ',
        mystr,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )

    all_seats=rou.booked_seats+','+temp_str
    rou.booked_seats=all_seats
    arr = all_seats.split(',')
    rou.remaining_seats = 45-len(arr)
    rou.save()

    booking_details= buyticket(route_forign=rou,username=username, phone=phone, cnic=cnic, email= email ,amount=total_amount, noofseats=noofseats)
    booking_details.save()
    return redirect( '/userticket')
    # return redirect('/')

def ticket_buy_done(request, id):
    # bt = Bt.objects.get(pk=id)
    # bt.delete()
    temp_str = ""
    username= request.GET.get('username')
    phone = request.GET.get('phone')
    cnic = request.GET.get('cnic')
    email= request.GET.get('email')
    # amount = request.GET.get('amount')
    seatsno = request.GET.get('seatsno')
    noofseats = request.GET.getlist('checks[]')
    print('\nSeat booked are ',noofseats)
    # total_amount = noofseats.count()
    total_amount=0
    for i in noofseats:
        temp_str=temp_str+str(i)+","
        total_amount=total_amount+1
    temp_str = temp_str[:-1]

    noofseats=str(temp_str)
    rou=routee.objects.get(pk=id)
    total_amount=total_amount*rou.price
    if request.session.get('total_amount'):
        del request.session['total_amount']

    request.session['total_amount'] = str(total_amount)
    print('\n\n\nTotal amount = ',request.session['total_amount'])
    # check_verification_code(num)
    mystr = "Hello your ticket has been booked successfully " + "\nEmail: "+ email +"\nName: " + username + "\nPhone: " + phone + "\nCNIC: "+ cnic + "\nSeats booked are: "+ temp_str + "\nPrice: " + str(total_amount)
    send_mail(
        'Ticket confirmation ',
        mystr,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )

    all_seats=rou.buy_seats+','+temp_str
    rou.buy_seats=all_seats
    arr = all_seats.split(',')
    rou.remaining_seats = 45-len(arr)
    rou.save()

    buying_details= buyticket(route_forign=rou,username=username, phone=phone, cnic=cnic, email= email ,amount=total_amount, noofseats=noofseats)
    buying_details.save()
    return redirect( '/stripehome')
    # return redirect('/')


def useredit(request):
    email = request.session['email']
    if request.session.get('email'):
        cus = Customer.objects.get(email=email)
        context ={
            'cus':cus
        }
        return render(request, 'useredit.html', context)


def user_update(request):
    email = request.session['email']
    if request.session.get('email'):
        cus = Customer.objects.get(email=email)
        # cus = Company.objects.get(cus_id=com_id)
        cus.firstname = request.GET['title']
        cus.lastname = request.GET['price']
        cus.password = request.GET['author']
        cus.confirmpassword = request.GET['cpass']
        cus.save()
        return redirect('/userticket')


def btedit(request):
    email = request.session['email']
    if request.session.get('email'):
        bt = Bt.objects.get(email=email)
        context = {
            'bt': bt
        }
        return render(request, 'btedit.html', context)


def bt_update(request):

    email = request.session['email']
    if request.session.get('email'):
        cus = Bt.objects.get(email=email)
        # cus = Company.objects.get(cus_id=com_id)

        cus.username = request.GET['title']
        cus.fnames = request.GET['price']
        cus.lnames = request.GET['author']
        cus.passwords = request.GET['cpass']
        cus.save()
        return redirect('/btticket')


def edit(request):
    return redirect('/deletebt')


def rootselectionn(request):
    # stations = Station.objects.filter(companyid=Company.objects.get(id=2))

    stations = Station.objects.all()
    s1 = request.GET['TeamComp1']
    s2 = request.GET['TeamComp2']

    all_routes = routee.objects.filter(to_route=Station.objects.get(id=s1),from_route=Station.objects.get(id=s2))

    if(all_routes.count()==0):
        print('No route found')
    else:
        for i in all_routes:
            print(i.bus_no)

    context = {
        'all_routes': all_routes,
        'stations':stations,
    }

    return render(request, 'adminsearch.html', context)

def admindelete(request, id):
    bt = routee.objects.get(pk=id)
    bt.delete()
    return render(request, 'adminsearch.html')




class HomePageView(TemplateView):
    template_name = 'stripeforuser.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request): # new
    if request.method == 'POST':
        amo = request.session['total_amount']
        # amo = int(amo1)
        charge = stripe.Charge.create(
            amount=amo,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        context = {
            'amo': str(amo*100),
        }
    return render(request, 'charge.html',context)


class HomePageView(TemplateView):
    template_name = 'stripeforuser.html'


class HomePageView(TemplateView):
    template_name = 'stripeforuser.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context