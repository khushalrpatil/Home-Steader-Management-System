from django.db import models

# Create your models here.
class Agency(models.Model):
    name = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to="images/", max_length=250, default=None, null=True
    )

    def __str__(self):
        return self.name
    
class Request(models.Model):
    agency=models.ForeignKey(Agency, on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    location=models.TextField()