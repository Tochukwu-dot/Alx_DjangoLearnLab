from django.db.models.base import Model as Model
from .models import Library, Book
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.
from django.contrib.auth import login
from typing import Any
from django.contrib.auth.forms import UserCreationForm
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
    

    # def get_context_data(self, **kwargs: Any):
    #     context = super().get_context_data(**kwargs)
    #     library = self.get_object()
    #     context ['library.books.all'] = library.books.all()
    #     return context

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
def is_admin(user):
    return UserProfile.objects.filter(user=user.id, role = 'admin').exists()

def is_librarian(user):
    return UserProfile.objects.filter(user=user.id, role = 'librarian').exists()

def is_member(user):
    return UserProfile.objects.filter(user=user.id, role = 'member').exists()

# Views for the user roles

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return HttpResponse('Admin Only View')

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return HttpResponse('Librarian Only View')

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return HttpResponse('Member Only View')