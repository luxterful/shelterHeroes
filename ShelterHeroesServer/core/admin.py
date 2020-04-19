from django.contrib import admin
from django import forms

from ShelterHeroesServer.users.models import User
from .models import Shelter, Animal, Post, Comment


@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    pass


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(AnimalAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields["followed_by"].widget = forms.CheckboxSelectMultiple()
        return form


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
