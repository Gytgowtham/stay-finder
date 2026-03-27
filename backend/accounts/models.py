from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):

    PROPERTY_TYPE_CHOICES = (
        ('PG', 'PG'),
        ('RENTAL', 'Rental House'),
        ('HOTEL', 'Hotel'),
    )

    AREA_TYPE_CHOICES = (
        ('URBAN', 'Urban'),
        ('RURAL', 'Rural'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=200)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    area_type = models.CharField(max_length=20, choices=AREA_TYPE_CHOICES)
    city = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="properties/", null=True, blank=True)


    def __str__(self):
        return self.title
    