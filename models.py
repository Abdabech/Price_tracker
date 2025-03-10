from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLFIeld()

    def __str__(self):
        return self.name