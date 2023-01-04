from django.contrib import admin
from books.models import Sessoes
from books.models import Books
from books.models import Posts


# Register your models here.

admin.site.register(Sessoes)
admin.site.register(Books)
admin.site.register(Posts)


