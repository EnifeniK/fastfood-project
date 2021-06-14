from django.shortcuts import render
from .models import Meal


def home(request):
    return render(request, 'food/home.html')


def mealpage(request):
    meals = Meal.objects.all()
    return render(request, 'food/meals.html', {'meals': meals})


def aboutpage(request):
    return render(request, 'food/aboutinfo.html')


def orderpage(request):
    return render(request, 'food/orders.html')


def objective(request):
    return render(request, 'food/objectivepage.html')


def promises(request):
    return render(request, 'food/promisepage.html')


def ourreviews(request):
    return render(request, 'food/ourreviews.html')