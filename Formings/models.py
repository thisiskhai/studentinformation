from django.db import models

# Create your models here.
class Forming(models.Model):
    name = models.CharField(max_length=120)
    phoneNumber = models.CharField(max_length=10)
    className = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    note = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name