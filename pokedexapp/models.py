from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=300)
    url = models.CharField(max_length=250)

    def __str__(self):
        return self.name