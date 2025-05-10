from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField(max_length=6)
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.booking_date}"
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.title} - {self.price}'