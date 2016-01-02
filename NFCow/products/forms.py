from django import forms

class ProductForm(forms.Form):
	quantity = forms.IntegerField(initial = 1)