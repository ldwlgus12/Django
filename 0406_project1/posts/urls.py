from django.urls import path
from . import views

app_name='posts'
urlpatterns = [
    path('', views.base, name='base'),
    path('category/<str:subject>/', views.category, name='category'),
    path('detail/<int:post_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('update/<int:post_pk>/', views.update, name='update'),
    path('delete/<int:post_pk>/', views.delete, name='delete'),
]
