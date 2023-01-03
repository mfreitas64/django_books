from django.shortcuts import redirect
from django.urls import reverse_lazy

class ValidateUsersPermissions(object):
    permission_required = ('books.add_sessoes', 'books.delete_sessoes',
                            'books.update_sessoes', 'books.add_books',
                            'books.delete_books', 'books.update_books')
    url_redirect = None

    def get_perms(self):
        if isinstance(self.permission_required,str): return(self.permission_required)
        else: return self.permission_required

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('book:denied')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        return redirect(self.get_url_redirect())
