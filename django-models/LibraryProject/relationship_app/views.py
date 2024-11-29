from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import DetailView
from typing import Any
from django.db.models.query import QuerySet
# Create your views here.

# function-based view
def book_list_view (request):
    """ lists all books stored in the database. """
    books = Book.objects.all()
    context = {'book' : books}
    template = 'relationship_app/list_books.html'
    return render (request, template_name = template, context = context)

# class_based view

class LibraryDetailView(DetailView):
    """ Returns information for a specific library"""
    template_name = 'library_detail.html'
    model = Library
    context_object_name = 'library'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        library = Library.objects.get()
        context ['books'] = library.books.all()
        return context
    