from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomerProfile(models.Model):
    user = models.OneToOneField(User)
    direccion = models.TextField(blank=True)
    admin = models.NullBooleanField()
    profile_picture = models.ImageField(upload_to='Customers', blank=True)
    
    def __str__(self):
        return self.user.username