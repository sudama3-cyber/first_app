from django.urls import path
from . import views

app_name = 'posts' # アプリケーション内で使用する名前空間を定義

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'), # トップページのURLパターンと対応するview
  path('create/', views.CreateView.as_view(), name='create'),
]