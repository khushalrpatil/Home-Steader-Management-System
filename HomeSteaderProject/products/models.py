from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    CHOICES = [
        ("Crop", "Crop"),
        ("Herb", "Herb"),
        ("Fertilizer", "Fertilizer"),
        ("Vegetable", "Vegetable"),
        ("Seed", "Seed"),
        ("Fruit", "Fruit"),
    ]
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=30, choices=CHOICES)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(
        upload_to="images/", max_length=250, default=None, null=True
    )

    def __str__(self):
        return self.name


class Report(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    user = models.CharField(max_length=150)
    product = models.CharField(max_length=50)
    quantity = models.IntegerField(null=True, blank=True, default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=30,
        choices=[
            ("Delivered", "Delivered"),
            ("Pending", "Pending"),
        ],
        default="Pending",
    )
    phone = models.IntegerField(null=True, blank=True, default=1)
    city = models.CharField(max_length=150, default="Sanaswadi")
    state = models.CharField(max_length=150, default="Maharashtra")
    zip = models.CharField(max_length=150, default="412208")
    street = models.CharField(max_length=150, default="Kalubai Nagar")
    


# class Cart(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
