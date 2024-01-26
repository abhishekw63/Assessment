from django.db import models

# Create your models here.

class Example(models.Model):
    title=models.CharField(max_length=255)
    code=models.TextField()
    lineons=models.BooleanField()
    language=models.CharField(max_length=255)
    style=models.CharField(max_length=255)

    def __str__(self):
        return self.title
