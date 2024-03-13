from django.urls import path
from . import views

urlpatterns = [
     path('', views.librarian_login, name='librarian_login'),
     path('logout/', views.librarian_logout, name='librarian_logout'),
    path('dashboard/', views.librarian_dashboard, name='librarian_dashboard'),
     path('approve_request/<int:request_id>/', views.approve_request, name='approve_request'),
     path('delete_request/<int:request_id>/', views.delete_book_request, name='delete_book_request'),
]
