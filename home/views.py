from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "app/index.html")

def MensTeam(request):
    return render(request, "app/MensTeam.html")

def WomensTeam(request):
    return render(request, "app/WomensTeam.html")

def AboutOrganisation(request):
    return render(request, "app/AboutOrganisation.html")

def Grassroots(request):
    return render(request, "app/Grassroots.html")

def OurLocations(request):
    return render(request, "app/OurLocations.html")

def ContactUs(request):
    return render(request,"app/ContactUs.html")