from django.db import models


class People(models.Model):
    name = models.CharField(max_length=255)
    document = models.CharField(max_length=11)
