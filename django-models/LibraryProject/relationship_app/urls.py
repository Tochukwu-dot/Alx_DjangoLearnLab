from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('books/list-of-books/', view=views.book_list_view),
    path('library/library-detail/<int:pk>/', views.LibraryDetailView.as_view())
]