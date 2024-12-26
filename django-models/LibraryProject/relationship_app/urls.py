from django.urls import path
from . import views
from .views import LoginView, LogoutView, book_list_view, LibraryDetailView, add_book, edit_book, delete_book

urlpatterns = [
    path('books/list-of-books/', view=views.book_list_view),
    path('library/library-detail/<int:pk>/', views.LibraryDetailView.as_view()),

    #url paths for authentication and registration
    path('accounts/login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('accounts/register/', views.register.as_view(template_name='relationship_app/register.html'), name='register'),

    #paths to the role-based views
    path('admin-only/', views.admin_view, name = 'admin only'),
    path('librarian-only/', views.librarian_view, name = 'librarian only'),
    path('member-only/', views.member_view, name = 'member only'),

    #paths to the permissions
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
]
