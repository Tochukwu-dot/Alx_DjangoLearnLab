from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('books/list-of-books/', view=views.book_list_view),
    path('library/library-detail/<int:pk>/', views.LibraryDetailView.as_view()),

    #url paths for authentication and registration
    path('accounts/login/', views.AppLogin.as_view(), name='login'),
    path('accounts/logout/', views.AppLogout.as_view(), name='logout'),
    path('accounts/register/', views.Register.as_view(), name='register')
]