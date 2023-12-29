from django.urls import path
from . import views

urlpatterns = [
    path('meal/',views.home,name='index'),
    
]


