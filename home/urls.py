from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("",views.home,name='home'),
    path("MensTeam",views.MensTeam,name='MensTeam'),
    path("WomensTeam",views.WomensTeam,name='WomensTeam'),
    path("AboutOrganisation",views.AboutOrganisation,name='AboutOrganisation'),
    path("Grassroots",views.Grassroots,name='Grassroots'),
    path("OurLocations",views.OurLocations,name='OurLocations'),
    path("ContactUs", views.ContactUs,name='ContactUs')
]
