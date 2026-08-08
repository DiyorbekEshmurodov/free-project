from tkinter import Place
from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from geopy.distance import geodesic
from .models import *
from forms import *


def login_required_decorator(func):
    return login_required(func,login_url='login_page')

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page')

    return render (request,'login.html')

def home_page(request):
    return render(request,'home.html')

@login_required_decorator
def hisobot_create(request):
    model = Hisobot()
    form = HisobotForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('hisobot_list')

    return render(request,'hisobot.html')

@login_required_decorator
def get_place(request):
    user_lat=request.POST.get('lat')
    user_lon=request.POST.get('lng')

    if not user_lat or not user_lon:
        return JsonResponse({"error":"Koordinatalar tuliq yuborilmadi!"},status=400)

    user_location =(float(user_lat),float(user_lon))
    user_place = None
    min_distance = float('inf')

    for place in Place.objects.all():
        place_location = (place.lat,place.lon)
        distance = geodesic(user_location,place_location).km

        if distance < min_distance:
            min_distance = distance
            user_place = place
    if user_place:
        return JsonResponse({
            'success': True,
            'user_place':user_place.name,
            'distance_km': round(min_distance,2)
        })
    else:
        return JsonResponse({'message':"Bazada hech qanday joy topilmadi"})