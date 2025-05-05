from django.urls import path
from restaurant import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
]