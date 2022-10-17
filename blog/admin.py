from django.contrib import admin
from .models import Book, Post, Comment

# Register your models here.
# from django.contrib import admin

admin.site.register(Book)
#admin.site.register(Post)0410

#Customizing the way that models are displayed
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','publish','status')
    list_filter=('status','created','publish','author')
    search_fields = ('title','body')
    prepopulated_fields={'slug':('title',)}
    raw_id_fields =('author',)
    date_hierarchy= "publish"
    ordering=('status','publish',)

@admin.register(Comment)
class CommmentAdmin(admin.ModelAdmin):
        list_display=('name','email','post','created','active')
        list_filter=('active','created','updated')
        search_fields=('name','email','body')

