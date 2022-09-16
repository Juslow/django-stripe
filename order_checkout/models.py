from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}, price: {self.price}$"



