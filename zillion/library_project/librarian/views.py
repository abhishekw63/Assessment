from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from library.models import Book, BookRequest
from django.contrib.auth.decorators import login_required

def librarian_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in as a librarian.')
            return redirect('librarian_dashboard')  
        else:
            messages.error(request, 'Invalid username or password for librarian.')
    return render(request, 'librarian_login.html')  

@login_required
def librarian_dashboard(request):
    books = Book.objects.all()
    book_requests = BookRequest.objects.filter(approved=False)
    
    return render(request, 'librarian_dashboard.html', {'books': books, 'book_requests': book_requests})

def librarian_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('librarian_login') 

def approve_request(request, request_id):
    book_request = get_object_or_404(BookRequest, id=request_id)
    book_request.approved = True
    book_request.save()
    return redirect('librarian_dashboard')

def delete_book_request(request, request_id):
    book_request = get_object_or_404(BookRequest, id=request_id)
    book_request.delete()
    return redirect('librarian_dashboard')