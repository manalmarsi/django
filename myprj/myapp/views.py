from django.shortcuts import render
from django.http import HttpResponse
from .models import Employe

# Create your views here.
def home(request):
    return render(request,"home.html")

def employee_list(request):
    employees = Employe.objects.all()  # Récupère tous les employés
<<<<<<< HEAD
    return render(request, 'employeelist.html', {'employees': employees})
=======
    return render(request, 'employeelist.html', {'employees': employees})
>>>>>>> f40ded6063f4fde36eafc1953ad440b90930e5e9
