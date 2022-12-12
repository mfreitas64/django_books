from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Sessoes, Books

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'books/index.html'
    model = Sessoes
    context_object_name = 'displaybook'

    def get_queryset(self):
        """Return the last five published Books."""
        return Sessoes.objects.order_by('sessao_date')[:5]

class DetailView(generic.DetailView):
    model = Sessoes
    template_name = 'books/detalhe.html'

class DetalhesLivro(DetailView):
    model = Books
    template_name = 'books/detalhe_livro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def about(request):
    return render(request, 'books/about.html', {'title': 'About'})
