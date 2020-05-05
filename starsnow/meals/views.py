from django.shortcuts import render

from .models import Meals

# Create your views here.

def home(request):

    #return HttpResponse('<h1> Starsnowice home </h1>')
    return render(request,'design/home.html')
#difference between return render and return Httresponse is
#render can take argument of template and context, usually render is better


def meal_list(request):
    meal_list = Meals.objects.all()

    context = {'meal_list':meal_list,}

    return render(request,'Meals/list.html',context)

def meal_detail(request,slug):
    meal_detail = Meals.objects.get(slug = slug)

    context = {'meal_detail':meal_detail}

    return render(request, 'Meals/detail.html', context)

def location(request):
    return render(request,'location/map.html')
