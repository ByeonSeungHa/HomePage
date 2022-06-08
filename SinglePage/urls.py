from django.urls import path
from . import views

urlpatterns = [
    path('', views.SinglePage),
    path('SinglePage2/', views.SinglePage2),
    path('SinglePage3/', views.SinglePage3),
]