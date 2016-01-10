from userprofiles.models import CustomerProfile

def customer_avatar(request):
	if request.user.is_anonymous():
		return {'avatar' : None }
	
	q_customer = CustomerProfile.objects.filter(user = request.user)
	if not q_customer:
		q_customer = CustomerProfile.objects.create(user = request.user)

		
	customer = CustomerProfile.objects.filter(user__username = request.user.username)[0]
	
	return {'avatar' : customer.avatar}