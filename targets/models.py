from django.db import models


class Target(models.Model):
    nome = models.CharField(max_length=100)
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    def __str__(self):
        return self.description