from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomerProfileManager(models.Manager):
	def update_customer_profile(self, my_name, avatar, user):
		self.filter(user__username = user).update(nombre = my_name, avatar = avatar)

class CustomerProfile(models.Model):
    user = models.OneToOneField(User)
    nombre = models.CharField(blank = True, max_length = 100)
    avatar = models.ImageField(upload_to = 'Customers', blank=True)    
    
    objects = CustomerProfileManager()
    
    def avatar_url(self):
        return self.avatar.url
    
    def __str__(self):
        return "%s's profile" % self.user