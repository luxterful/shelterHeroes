from PIL import Image

from django.core.management.base import BaseCommand, CommandError
from django.core import management
from django.core.files import File
from django.core.files.base import ContentFile

from ShelterHeroesServer.users.models import User
from ShelterHeroesServer.core.models import Shelter, Animal, Post
from ShelterHeroesServer.storage.models import PostImage


class Command(BaseCommand):
    help = "Create initial database data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush", action="store_true", help="Flush database before",
        )

    def _add_post(self, animal, text, img_url, liked_by):
        img = PostImage()
        img.image_file.save("", File(open(img_url, "rb")))
        post = Post(posted_by=animal, text=text, image=img)
        post.save()
        post.liked_by.set(liked_by)
        post.save()

    def handle(self, *args, **options):
        if options["flush"]:
            # delete posts separately to also delte the image files
            posts = Post.objects.all()
            for post_obj in posts:
                post_obj.delete()
            management.call_command("flush", verbosity=0, interactive=False)

        user_admin = User.objects.create_superuser(
            email="admin@luxterful.eu", password="Matr1x42", full_name="Lukas",
        )
        user_admin.save()

        user_chuck = User.objects.create_user(
            email="harry@labby.com", password="qwerty", full_name="Harry",
        )
        user_chuck.save()

        user_peter = User.objects.create_user(
            email="peter@bauer.net", password="qwerty", full_name="Peter",
        )
        user_peter.save()

        user_norris = User.objects.create_user(
            email="chuck@norris.war", password="qwerty", full_name="Chuck",
        )
        user_norris.save()

        shelter_neubrunn = Shelter(
            name="Tierfreunde Neubrunn", address="Daheim in Neubrunn", admin=user_admin
        )
        shelter_neubrunn.save()

        animal_bjarne = Animal(name="Bjarn", race="cute Dog", shelter=shelter_neubrunn)
        animal_bjarne.save()
        animal_bjarne.followed_by.set((user_admin, user_chuck, user_norris, user_peter))

        animal_derp = Animal(name="Chico", race="crazy Dog", shelter=shelter_neubrunn)
        animal_derp.save()
        animal_derp.followed_by.set((user_admin, user_chuck, user_norris, user_peter))

        animal_toni = Animal(name="Toni", race="süßer Hund", shelter=shelter_neubrunn)
        animal_toni.save()
        animal_toni.followed_by.set((user_admin,))

        # -----
        self._add_post(
            animal_bjarne,
            "Was geht?",
            "./ShelterHeroesServer/static/demo_images/bjarne-1.jpg",
            [user_admin, user_chuck],
        )

        # -----
        self._add_post(
            animal_bjarne,
            "Chillin!",
            "./ShelterHeroesServer/static/demo_images/bjarne-2.jpg",
            [user_admin, user_chuck],
        )

        # -----
        self._add_post(
            animal_derp,
            "Sup?",
            "./ShelterHeroesServer/static/demo_images/chico-1.jpg",
            [user_admin, user_chuck],
        )

        # -----
        self._add_post(
            animal_derp,
            "Was ist das?",
            "./ShelterHeroesServer/static/demo_images/chico-2.jpg",
            [user_admin, user_chuck],
        )

        # -----
        self._add_post(
            animal_toni,
            "Hey Ladies",
            "./ShelterHeroesServer/static/demo_images/toni-1.jpg",
            [user_admin, user_chuck],
        )

        # -----
        self._add_post(
            animal_toni,
            "Woof",
            "./ShelterHeroesServer/static/demo_images/toni-2.jpg",
            [user_admin, user_chuck],
        )

        # -----
        self._add_post(
            animal_toni,
            "Ich mach heute parteeyy",
            "./ShelterHeroesServer/static/demo_images/toni-3.jpg",
            [user_admin, user_chuck],
        )
