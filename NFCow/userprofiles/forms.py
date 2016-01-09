from django.forms import ModelForm
from .models import CustomerProfile

class CustomerProfileForm(ModelForm):
	class Meta:
		model = CustomerProfile
		fields = ['nombre', 'avatar']
	# name = forms.CharField(max_length = 100)
	# avatar = forms.ImageField()
	