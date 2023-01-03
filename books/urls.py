from django.urls import path
from . import views
from . views import (SessoesCreateView, BooksCreateView)

app_name = 'book'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.about, name='Books-About'),
    path('denied/', views.denied, name='denied'),
    path('<int:pk>/', views.DetailView.as_view(), name='detalhe'),
    path('novasessao/', SessoesCreateView.as_view(), name='criar-sessao'),
    path('novolivro/', BooksCreateView.as_view(), name='criar-livro'),
    path('detalhe_livro/<int:pk>/', views.DetalhesLivro.as_view(), name='detalhe_livro'),
]