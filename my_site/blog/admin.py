from django.contrib import admin
from .models import Tag,Author,Post,Comments

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter=("author","tags",'date') #in RHS panel there will be filters
    list_display=('title','date','author') #display post as these 3 columns
    prepopulated_fields={"slug":("title",)} #to prepopulated slug. key should match field

class CommentsAdmin(admin.ModelAdmin):
    list_display=('user_name','post')
      
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Comments,CommentsAdmin)
