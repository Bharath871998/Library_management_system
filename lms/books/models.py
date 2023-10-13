from django.db import models
from django.utils import timezone


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length = 20,)
    author = models.CharField(max_length=20)
    price = models.IntegerField()
    publish = models.DateTimeField(default=timezone.now)
    STOCK_CHOICE = (
        ('available', 'Available'),
        ('out of stock', 'Out Of Stock')
    )
    stock = models.CharField(max_length=50,choices=STOCK_CHOICE,default='draft')

    def __str__(self):
        return  self.name