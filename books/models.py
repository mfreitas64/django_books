from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Sessoes(models.Model):
    title = models.CharField(max_length=100)
    sessao_date = models.DateField()
    
    def __str__(self):
        return self.title

class Books(models.Model):
    sessaoid = models.ForeignKey(Sessoes, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=50, default='Autor')
    description = models.CharField(max_length=250)
    sinopse = models.TextField()
    image = models.ImageField(upload_to='books/')
#   presented_by = models.CharField(max_length=50, default='Autor')
    presented_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('book:detalhe_livro', kwargs={'pk': self.pk})

class Posts(models.Model):
    bookid = models.ForeignKey(Books, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content =models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book:index')