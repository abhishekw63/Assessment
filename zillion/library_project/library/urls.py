from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('request_book/<int:book_id>/', views.request_book, name='request_book'),

  
]
