from django.urls import path,include
from .views import ExampleListView

urlpatterns = [
    path('<int:pk>/',ExampleListView.as_view()),
    path('',ExampleListView.as_view())
    
]