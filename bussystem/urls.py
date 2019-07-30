from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('dashboard/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registrationforuser/', views.registrationforuser, name='registrationforuser'),
    path('companyregister/', views.companyregister, name='companyregister'),
    path('create/', views.create, name='create'),
    path('authentication/', views.authentication, name='authentication'),
    path('btticket/', views.btticket, name='btticket'),
    path('cancel/', views.btcancel, name='btcancel'),
    path('deletebt/', views.deletebt, name='deletebt'),
    path('usercancel/', views.usercancel, name='usercancel'),
    path('userticket/', views.userticket, name='userticket'),
    path('createbt/', views.createbt, name='createbt'),
    path('delete/<id>/', views.delete, name='delete'),
    path('adminprofile/', views.adminprofile, name='adminprofile'),
    path('performance/', views.performance, name='performance'),
    path('addthings/', views.addthings, name='addthings'),
    path('routes/', views.routes, name='routes'),
    path('station/', views.station, name='station'),
    path('adminsearch/', views.adminsearch, name='adminsearch'),
    path('signout/', views.signout, name='signout'),

]