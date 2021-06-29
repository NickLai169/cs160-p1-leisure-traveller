from django.shortcuts import render, resolve_url
from django.http import HttpResponse

def forecast(request):
    return render(request, 'weather/forecast.html')

def forecast_alert(request):
    return render(request, 'weather/forecast-alert.html')

def comparison(request):
    return render(request, 'weather/comparison.html')

def comparison_alert(request):
    return render(request, 'weather/comparison-alert.html')

def index(request):
    return render(request, 'weather/index.html')

def landing(request):
    return render(request, 'weather/landing.html')

def trip_planner(request):
    return render(request, 'weather/trip-planner-day.html')