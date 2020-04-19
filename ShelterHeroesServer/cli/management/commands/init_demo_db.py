from PIL import Image

from django.core.management.base import BaseCommand, CommandError
from django.core import management
from django.core.files import File
from django.core.files.base import ContentFile

from ShelterHeroesServer.users.models import User
from ShelterHeroesServer.core.models import Shelter, Animal, Post


class Command(BaseCommand):
    help = "Create initial database data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush", action="store_true", help="Flush database before",
        )

    def handle(self, *args, **options):
        if options["flush"]:
            # delete posts separately to also delte the image files
            posts = Post.objects.all()
            for post_obj in posts:
                post_obj.delete()
            management.call_command("flush", verbosity=0, interactive=False)

        user_admin = User.objects.create_superuser(
            email="admin@luxterful.eu", password="Matr1x42", full_name="Lukas B.",
        )
        user_admin.save()

        user_chuck = User.objects.create_user(
            email="chuck@labby.com", password="Matr1x42", full_name="Chuck van Labby",
        )
        user_chuck.save()

        user_peter = User.objects.create_user(
            email="peter@bauer.net", password="Matr1x42", full_name="Peter Landwirt",
        )
        user_peter.save()

        user_norris = User.objects.create_user(
            email="chuck@norris.war", password="Matr1x42", full_name="Chuck Norris",
        )
        user_norris.save()

        shelter_neubrunn = Shelter(
            name="Tierfreunde Neubrunn", address="Daheim in Neubrunn", admin=user_admin
        )
        shelter_neubrunn.save()

        animal_bjarne = Animal(name="Bjarn", race="cute Dog", shelter=shelter_neubrunn)
        animal_bjarne.save()
        animal_bjarne.followed_by.set((user_admin,))

        animal_derp = Animal(name="Derpdog", race="crazy Dog", shelter=shelter_neubrunn)
        animal_derp.save()

        animal_toni = Animal(name="Toni", race="süßer Hund", shelter=shelter_neubrunn)
        animal_toni.save()

        # -----
        post_bjarne = Post(posted_by=animal_bjarne, text="Was geht?")
        post_bjarne.image.save(
            "x.jpg",
            File(
                open(
                    "./ShelterHeroesServer/cli/management/commands/demo_images/bjarne-1.jpg",
                    "rb",
                )
            ),
        )
        post_bjarne.liked_by.set([user_admin, user_chuck])
        post_bjarne.save()

        # -----
        post2_bjarne = Post(posted_by=animal_bjarne, text="Chillin!")
        post2_bjarne.image.save(
            "x.jpg",
            File(
                open(
                    "./ShelterHeroesServer/cli/management/commands/demo_images/bjarne-2.jpg",
                    "rb",
                )
            ),
        )
        post2_bjarne.liked_by.set([user_admin, user_chuck])
        post2_bjarne.save()

        # -----
        post_chico = Post(posted_by=animal_derp, text="Sup?")
        post_chico.image.save(
            "x.jpg",
            File(
                open(
                    "./ShelterHeroesServer/cli/management/commands/demo_images/chico-1.jpg",
                    "rb",
                )
            ),
        )
        post_chico.liked_by.set([user_admin, user_chuck])
        post_chico.save()

        # -----
        post2_chico = Post(posted_by=animal_derp, text="Was ist das?")
        post2_chico.image.save(
            "x.jpg",
            File(
                open(
                    "./ShelterHeroesServer/cli/management/commands/demo_images/chico-2.jpg",
                    "rb",
                )
            ),
        )
        post2_chico.liked_by.set([user_admin, user_chuck])
        post2_chico.save()

        # -----
        post_toni = Post(posted_by=animal_toni, text="Hey Ladies")
        post_toni.image.save(
            "x.jpg",
            File(
                open(
                    "./ShelterHeroesServer/cli/management/commands/demo_images/toni-1.jpg",
                    "rb",
                )
            ),
        )
        post_toni.liked_by.set([user_admin, user_chuck])
        post_toni.save()

        # -----
        post2_toni = Post(posted_by=animal_toni, text="Woof")
        post2_toni.image.save(
            "x.jpg",
            File(
                open(
                    "./ShelterHeroesServer/cli/management/commands/demo_images/toni-2.jpg",
                    "rb",
                )
            ),
        )
        post2_toni.liked_by.set([user_admin, user_chuck])
        post2_toni.save()

        # -----
        post3_toni = Post(posted_by=animal_toni, text="Ich mach heute parteeyy")
        post3_toni.image.save(
            "x.jpg",
            File(
                open(
                    "./ShelterHeroesServer/cli/management/commands/demo_images/toni-3.jpg",
                    "rb",
                )
            ),
        )
        post3_toni.liked_by.set([user_admin, user_chuck])
        post3_toni.save()
