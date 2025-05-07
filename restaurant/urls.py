from django.urls import path
from restaurant import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]