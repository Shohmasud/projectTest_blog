from django.contrib import admin
from .models import Comments,Blog
# Register your models here.
class Admin_Blog(admin.ModelAdmin):
    list_display = ('id', 'nameBlog','textBlog','showBlog')
    search_fields = ['id','nameBlog','textBlog','showBlog ']
admin.site.register(Blog,Admin_Blog)

class Admin_Comment(admin.ModelAdmin):
    list_display = ('id', 'body','created_on','parent',)
    search_fields = ['id','body','created_on']
admin.site.register(Comments, Admin_Comment)