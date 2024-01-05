from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator

# Create your models here.

class Tag(models.Model):
    caption=models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f'{self.caption}'
    
class Author(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email_address=models.EmailField()
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
class Post(models.Model):
    title=models.CharField(max_length=20)
    excerpt=models.CharField(max_length=150)
    #image_name=models.CharField(max_length=100) 
    image=models.ImageField(null=True, upload_to='posts') #change from image_name
    date=models.DateField(auto_now=True) #auto update date
    slug=models.SlugField(unique=True,db_index=True) #can db_index because by default it is true. unique=true implies same
    #content=models.TextField(MinLengthValidator(10)) #displaying django.core.validators.MinLengthValidator object at 0x00000226C076CF50>:
    content=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,related_name="posts") #adding a relation one to many that is Author to Post
    tags=models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title
    


class Comments(models.Model):
    user_name=models.CharField(max_length=120)
    user_email=models.EmailField()
    text=models.TextField(max_length=500)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
            
    