import uuid
from PIL import Image
from io import BytesIO

from django.dispatch import receiver
from django.conf import settings
from django.db import models
from django.db.models.signals import post_delete
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile


def scramble_filename(instance, filename):
    return f"posts/{uuid.uuid4()}.jpg"


# Create your models here.
class PostImage(models.Model):
    image_file = models.ImageField(upload_to=scramble_filename)

    def save(self):
        if self.image_file:
            image = Image.open(self.image_file)

            width, height = image.size
            if 250 > width > 2500 or 250 > height > 2500:
                raise ValidationError(
                    "Wrong imagesize. Each side must be between 250px and 2500px"
                )

            if image.format != "JPEG":
                image = image.convert("RGB")
                buffer = BytesIO()
                image.save(buffer, format="JPEG", quality=95)
                buffer.seek(0)

                self.image_file = InMemoryUploadedFile(
                    buffer,  # file
                    None,  # field_name
                    "whatever.jpg",  # file name, will be renamed anyways
                    "image/jpeg",  # content_type
                    buffer.tell,  # size
                    None,
                )

            super().save()
        else:
            raise ValidationError("Image is a mandatory field")


@receiver(post_delete, sender=PostImage)
def photo_post_delete_handler(sender, **kwargs):
    instance = kwargs["instance"]
    storage, path = instance.image.storage, instance.image.path
    if path.startswith(settings.MEDIA_ROOT):
        storage.delete(path)
