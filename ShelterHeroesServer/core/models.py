import uuid
from PIL import Image

from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings

from ShelterHeroesServer.users.models import User


class Shelter(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=50)
    race = models.CharField(max_length=50)
    origin = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    followed_by = models.ManyToManyField(User, blank=True, related_name="follows")

    def __str__(self):
        return self.name


class Post(models.Model):
    def scramble_filename(instance, filename):
        return f"{uuid.uuid4()}.jpg"

    posted_by = models.ForeignKey(
        Animal, related_name="posts", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to=scramble_filename)
    text = models.CharField(max_length=500)
    liked_by = models.ManyToManyField(User, blank=True)

    def save(self, *args, **kwargs):
        if self.image:
            image = Image.open(self.image)

            if image.format != "JPEG":
                raise ValidationError("wrong file type. only jpg/jpeg files allowed.")

            width, height = image.size
            if 250 > width > 2500 or 250 > height > 2500 or height != width:
                raise ValidationError(
                    "Wrong imagesize. Must be square between 250x250 and 2500x2500"
                )

            super().save(*args, **kwargs)
        else:
            raise ValidationError("Image is a mandatory field")


@receiver(post_delete, sender=Post)
def photo_post_delete_handler(sender, **kwargs):
    instance = kwargs["instance"]
    storage, path = instance.image.storage, instance.image.path
    if path.startswith(settings.MEDIA_ROOT):
        storage.delete(path)


class Comment(models.Model):
    text = models.CharField(max_length=500)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
