#!/usr/bin/env python3
import os

# initialize the django environment
# assumes ./proj/settings.py is your settings file, relative to current dir
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()

# import models and run django/python commands
from homepage import models as hmod


names = ['baby',
         'bungie',
         'cove',
         'fall',
         'fish1',
         'horse',
         'ice',
         'jump',
         'kid',
         'lights',
         'shark',
         'speed',
         'splash',
         'surf',
         'swimmers',
         'turtle',
         'whale',
         ]

for name in names:
    try:
        image = hmod.GalleryImage.objects.get(title=name)
        print("Image " + image.title + " already exists")
    except hmod.GalleryImage.DoesNotExist:
        image = hmod.GalleryImage()
        image.title = name
        image.filename = image.title + ".jpg"
        image.file_path = "images/" + image.filename
        image.size = 1.3
        image.mime_type = "image/jpg"
        image.save()
        print("Image " + image.title + " created")
