from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import F
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from .mixins import ValidateUsersPermissions
from .models import Sessoes, Books
from django.contrib import messages

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'books/index.html'
    model = Sessoes
    context_object_name = 'displaybook'

    def get_queryset(self):
        """Return the last five published Books."""
        return Sessoes.objects.order_by('sessao_date')[:10]

class DetailView(generic.DetailView):
    model = Sessoes
    template_name = 'books/detalhe.html'

class DetalhesLivro(DetailView):
    model = Books
    template_name = 'books/detalhe_livro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['sessao'] = Books.objects.select_related('sessaoid').get(pk=self.kwargs['pk'])
        return context

class SessoesCreateView(ValidateUsersPermissions, CreateView):
    model = Sessoes
    fields = ['title', 'sessao_date']
    
    def get_success_url(self):
        return reverse('book:index')

class BooksCreateView(ValidateUsersPermissions, CreateView):
    model = Books
    fields = ['sessaoid', 'book_name', 'author', 'description', 'sinopse', 'image']

    def form_valid(self, form):
        form.instance.presented_by = self.request.user
        form.save()
        return super().form_valid(form)

def about(request):
    return render(request, 'books/about.html', {'title': 'About'})

def denied(request):
    return render(request, 'books/denied.html', {'title': 'Acesso Restrito'})
