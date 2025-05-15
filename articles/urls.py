from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/nouveau/', views.ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/modifier/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('carte/', views.CarteView.as_view(), name='carte'),
    path('a-propos/', views.a_propos, name='a_propos'),
] 