from django.urls import path
from . import views

urlpatterns = [
    path('<int:num>/', views.number_print, name='number_print'),
]