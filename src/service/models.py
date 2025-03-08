from django.db import models
from mdeditor.fields import MDTextField

import random
import re


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    content = MDTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    @property
    def thumbnail(self):
        image_urls = []

        image_regex = r'!\[.*?\]\((.*?)\)'
        content = self.content

        images_in_content = re.findall(image_regex, content)
        
        # Add the found image URLs to the list
        image_urls.extend(images_in_content)

        if image_urls:
        # Pick a random image from the list
            random_image = random.choice(image_urls)
            return random_image
        else:
            return "/media/images/default.jpg"
