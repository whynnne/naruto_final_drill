from django.core.management.base import BaseCommand
from django.utils import timezone
from main.models import Village, Character, Jutsu

class Command(BaseCommand):
    help = 'Creates initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_initial_data()
        self.stdout.write(self.style.SUCCESS('Initial data has been created.'))

    def create_initial_data(self):
        # Create Villages
        leaf_village = Village.objects.create(name='Leaf Village', description='Home of Naruto')
        sand_village = Village.objects.create(name='Sand Village', description='Home of Gaara')

        # Create Characters
        naruto = Character.objects.create(
            name='Naruto Uzumaki',
            description='The main protagonist of the series.',
            date_of_birth=timezone.now(),
            power_level=100,
            rating=9.5,
            rarity='Legendary',
            village=leaf_village
        )

        gaara = Character.objects.create(
            name='Gaara',
            description='The Kazekage of the Sand Village.',
            date_of_birth=timezone.now(),
            power_level=95,
            rating=9.0,
            rarity='Epic',
            village=sand_village
        )

        sasuke = Character.objects.create(
            name='Sasuke Uchiha',
            description='A powerful ninja seeking revenge.',
            date_of_birth=timezone.now(),
            power_level=98,
            rating=9.2,
            rarity='Legendary',
            village=leaf_village
        )

        hinata = Character.objects.create(
            name='Hinata Hyuga',
            description='A skilled and kind-hearted ninja.',
            date_of_birth=timezone.now(),
            power_level=88,
            rating=8.5,
            rarity='Rare',
            village=leaf_village
        )

        sakura = Character.objects.create(
            name='Sakura Haruno',
            description='A medical ninja and a member of Team 7.',
            date_of_birth=timezone.now(),
            power_level=85,
            rating=8.0,
            rarity='Common',
            village=leaf_village
        )

        shikamaru = Character.objects.create(
            name='Shikamaru Nara',
            description='A lazy but highly intelligent ninja.',
            date_of_birth=timezone.now(),
            power_level=90,
            rating=8.8,
            rarity='Rare',
            village=leaf_village
        )

        # Create Jutsus
        rasengan = Jutsu.objects.create(
            name='Rasengan',
            description='A powerful spinning chakra technique by Naruto.'
        )

        chidori = Jutsu.objects.create(
            name='Chidori',
            description='A lightning-based jutsu used by Sasuke.'
        )

        gentle_fist = Jutsu.objects.create(
            name='Gentle Fist',
            description='A taijutsu style used by Hinata.'
        )
