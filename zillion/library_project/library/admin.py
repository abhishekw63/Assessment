from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Book)
admin.site.register(BookRequest)
admin.site.register(UserProfile)