from django.urls import path

from . import views

urlpatterns = [
    path('forecast/', views.forecast, name='forecast'),
    path('forecast/alert/', views.forecast_alert, name='forecast_alert'),
    path('comparison/', views.comparison, name='comparison'),
    path('comparison/alert/', views.comparison_alert, name='comparison_alert'),
    path('', views.index, name='index'),
    path("landing/", views.landing, name="landing"),
    path("trip/", views.trip_planner, name="trip-planner"),
]