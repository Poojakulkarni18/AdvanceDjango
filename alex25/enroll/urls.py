from django.urls import path
from .import views

urlpatterns = [
    path('reg/', views.showformdata),
    path('pass/', views.sreg),
]