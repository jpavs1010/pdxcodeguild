from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    favorite_color = models.CharField(max_length=200)
    favorite_fruit = models.CharField(max_length=200)
    catch_phrase = models.CharField(max_length=200)

    def __str__(self):
        return self.name
