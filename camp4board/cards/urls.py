from django.urls import path
from . import views

urlpatterns = [
    path('', views.card_list, name='card_list'),
    path('add_card/', views.add_card, name='add_card'),
]
