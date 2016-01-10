from userprofiles.models import CustomerProfile

def customer_avatar(request):
	if request.user.is_anonymous():
		return {'avatar' : None }
		
	customer = CustomerProfile.objects.filter(user__username = request.user.username)[0]
	return {'avatar' : customer.avatar}