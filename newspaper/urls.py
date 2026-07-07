from django.urls import path
from . import views

urlpatterns = [
    path('daily-news/', views.daily_newspaper, name='daily_newspaper'),
]