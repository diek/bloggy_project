from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('slug', 'created_at', 'views')

admin.site.register(Post, PostAdmin)
