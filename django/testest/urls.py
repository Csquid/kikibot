from django.urls import path, include
from . import views

app_name = 'testest'

urlpatterns = [
    path('keyboard/', views.keyboard),
    path('message', views.answer),
]
