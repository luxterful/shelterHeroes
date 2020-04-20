from django.contrib import admin

from .models import PostImage


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
