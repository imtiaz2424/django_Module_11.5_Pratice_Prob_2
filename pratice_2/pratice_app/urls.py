from django.urls import path
from . import views

urlpatterns = [       
    path('', views.index, name = 'home'),
    path('meallist/', views.meallist, name = 'meallist'),
]