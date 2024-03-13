from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Book, BookRequest
from django.contrib import messages

def home(request): 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home')
    else:
        if request.user.is_authenticated:
            available_books = Book.objects.all()
            user_books = BookRequest.objects.filter(user=request.user, approved=True)
            return render(request, 'home.html', {'available_books': available_books, 'user_books': user_books})
        else:
            return render(request, 'login.html')

@login_required
def request_book(request, book_id):
    book = Book.objects.get(id=book_id)
    request_obj, created = BookRequest.objects.get_or_create(user=request.user, book=book)
    if created:     
        messages.success(request, "Request sent successfully.")
        return redirect('home')
    else:
        return redirect('home')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')



