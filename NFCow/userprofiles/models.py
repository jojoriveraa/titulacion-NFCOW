from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomerProfiles(models.Model):
    user = models.OneToOneField(User)
    direccion = models.TextField()
    profile_picture = models.ImageField(upload_to='Customers', blank=True)
    
    def __str__(self):
        return self.user.username