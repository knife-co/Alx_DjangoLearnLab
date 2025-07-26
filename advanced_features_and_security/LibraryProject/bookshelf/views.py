from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import ExampleForm

# Create your views here.

# View list
class BookListView(PermissionRequiredMixin, ListView):
    model = Book
    template_name = 'bookshelf/book_list.html'
    context_object_name = 'books'
    permissions_required = 'bookshelf.can_view'
    raise_exception = True

# Create book
class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    template_name = 'bookshelf/book_form.html'
    fields = ['title', 'author', 'publication_year']
    success_url = reverse_lazy('book_list')
    permission_required = 'bookshelf.can_create'
    raise_exception = True

# Update book
class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    template_name = 'bookshelf/book_form.html'
    fields = ['title', 'author', 'publication_year']
    success_url = reverse_lazy('book_list')
    permission_required = 'bookshelf.can_edit'
    raise_exception = True

# Delete book
class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'bookshelf/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
    permission_required = 'bookshelf.can_delete'
    raise_exception = True

class ExampleFormView(PermissionRequiredMixin, CreateView):
    model = Book
    form_class = ExampleForm
    template_name = 'bookshelf/form_example.html'
    success_url = reverse_lazy('book_list')
    permission_required = 'bookshelf.can_create'
    raise_exception = True

    def form_valid(self, form):
        return super().form_valid(form)

