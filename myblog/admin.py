from django.contrib import admin
from .models import Post, Cat

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ['title']} #позволяет автоматически заполнять поле url на основе поля title

admin.site.register(Post, PostAdmin)

