from django.db.models.base import Model as Model
from .models import Library, Book
from django.views.generic import DetailView, CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.
from django.contrib.auth import login
from typing import Any
from django.contrib.auth.forms import UserCreationForm, BookForm

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
    template_name = 'relationship_app/library_detail.html'
    model = Library
    
class Login(LoginView):
    template_name = 'relationship_app/login.html'
    success_url = 'profile'

class Logout(LogoutView):
    template_name = 'relationship_app/logout.html'

class register(CreateView):
    form_class = UserCreationForm()
    template_name = 'relationship_app/register.html'
    success_url = 'login'

# class ProfileView(TemplateView):
#     template_name = 'relationship_app/profile.html'

# Tests for Specific roles:
from relationship_app.models import UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

def is_admin(user):
    return user.UserProfile.role == 'Admin'

def is_librarian(user):
    return user.UserProfile.role == 'Librarian'

def is_member(user):
    return user.UserProfile.role == 'Member'

# Views for the user roles

@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return render (request, template_name='relationship_app/admin_view.html/')

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return render (request, template_name='relationship_app/librarian_view.html/')

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return render (request, template_name='relationship_app/member_view.html/')

# Adding permissions

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm()
        return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm(instance=book)
        return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})
