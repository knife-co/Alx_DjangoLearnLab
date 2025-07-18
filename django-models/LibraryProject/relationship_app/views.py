from django.shortcuts import render, redirect
from .form import RegisterForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register_view(request):
    if request.method = 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'relationship_app/register.html', {'form': form})

    