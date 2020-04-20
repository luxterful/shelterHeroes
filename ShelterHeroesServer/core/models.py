from django.db import models
from django.core.exceptions import ValidationError

from ShelterHeroesServer.users.models import User
from ShelterHeroesServer.storage.models import PostImage


class Shelter(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=50)
    image = models.ForeignKey(PostImage, null=True, on_delete=models.SET_NULL)
    race = models.CharField(max_length=50, null=True)
    origin = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    followed_by = models.ManyToManyField(User, blank=True, related_name="follows")

    def __str__(self):
        return self.name


class Post(models.Model):
    posted_by = models.ForeignKey(
        Animal, related_name="posts", on_delete=models.CASCADE
    )
    image = models.ForeignKey(PostImage, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=500)
    liked_by = models.ManyToManyField(User, blank=True)


class Comment(models.Model):
    text = models.CharField(max_length=500)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
