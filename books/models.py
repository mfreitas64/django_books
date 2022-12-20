from django.db import models

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
    presented_by = models.CharField(max_length=50, default='Autor')
