from django.urls import path

from . import views

app_name = 'book'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.about, name='Books-About'),
    path('<int:pk>/', views.DetailView.as_view(), name='detalhe'),
    path('detalhe_livro/<int:pk>/', views.DetalhesLivro.as_view(), name='detalhe_livro'),
]