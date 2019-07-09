from django.db import models

# Create your models here.
class Post(models.Model):
    # title = models.TextField()
    style_image = models.ImageField(upload_to='static/style_images',default="",)
    input_image = models.ImageField(upload_to='static/input_images',default="",)

