from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image_link = models.URLField(max_length=555)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
