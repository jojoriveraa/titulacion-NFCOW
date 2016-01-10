from userprofiles.models import CustomerProfile

def customer_avatar(request):
	customer = CustomerProfile.objects.filter(user__username = request.user.username)[0]
	return {'avatar' : customer.avatar_url}