from django.urls import path
from . import views

urlpatterns = [
    path('membros/', views.membros_list, name='membros_list'),
    path('membro/<int:pk>/', views.membro_detail, name='membro_detail'),
    path('reunioes/', views.reunioes_list, name='reunioes_list'),
    path('reuniao/<int:pk>/', views.reuniao_detail, name='reuniao_detail'),
]
