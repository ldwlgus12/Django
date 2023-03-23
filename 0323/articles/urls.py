from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    # 경로가 articles/articles/가 되기 때문에 어색하므로 articles는 지워도 무관

    path('<int:num>/', views.detail, name='detail'),
    path('<str:name>/', views.detail_name, name='detail_name'),
    
]