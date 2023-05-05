from django.shortcuts import render
from django.http import HttpResponse

from .models import Pet

def home(request):
    pets = Pet.objects.all()
    context = {"pets":pets}
    return render(request,"adoptions/home.html",context)


def pet_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    context = {'pet':pet}
    return render(request,"adoptions/pet_detail.html", context)
