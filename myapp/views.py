from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Car
from .forms import CarForm
# Create your views here.
def index(request):
    return render(request,"myapp/index.html",{
        'myapp':Car.objects.all()
    })


def view_car(request,id):
    car = Car.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            new_company = form.cleaned_data['Company']
            new_model = form.cleaned_data['model']
            new_year = form.cleaned_data['year']
            new_price = form.cleaned_data['Price']

            new_car = Car(
                Company = new_company,
                model = new_model,
                year=new_year,
                Price = new_price
            )
            new_car.save()
            return render(request,'myapp/add.html',{
                'form':CarForm(),
                'success':True
            })
        
    else:
        form = CarForm()
    return render(request,'myapp/add.html',{
        'form':CarForm()
    })