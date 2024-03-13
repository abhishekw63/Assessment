from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=25)
    author=models.CharField(max_length=25)
    pub_year=models.IntegerField()
    quantity=models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.title}'

class BookRequest(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)  
    book=models.ForeignKey(Book,on_delete=models.CASCADE)  
    request_date=models.DateTimeField(auto_now_add=True)
    renwal_date=models.DateTimeField(null=True,blank=True)
    approved=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.user.username}-{self.book.title}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_librarian = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username   
