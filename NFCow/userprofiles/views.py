from django.shortcuts import render, render_to_response, get_object_or_404

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse, HttpResponseRedirect

from django.template import RequestContext 

from .forms import CustomerProfileForm
from userprofiles.models import CustomerProfile

# Create your views here.

def ingresar(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/branches/1/')
	
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/branches/1/')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
	return render_to_response('login.html',{'formulario':formulario}, context_instance=RequestContext(request))

def registrar(request):
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/login')
	else:
		formulario = UserCreationForm()
	return render_to_response('signup.html',{'formulario':formulario}, context_instance=RequestContext(request))

def my_profile(request):
	if request.method=='POST':
		instance = get_object_or_404(CustomerProfile, user__username = request.user.username)
		formulario = CustomerProfileForm(request.POST, request.FILES, instance = instance)
		if formulario.is_valid:
			my_profile = formulario.save(commit=False)
			my_profile.avatar = request.FILES['avatar']
			my_profile.save()
			return HttpResponseRedirect('/my-profile')
	else:
		q_customer = CustomerProfile.objects.filter(user = request.user)[0]
		if not q_customer:
			q_customer = CustomerProfile.objects.create(user = request.user)
		formulario = CustomerProfileForm
	return render_to_response('my-profile.html',{'formulario':formulario, 'customer': q_customer}, context_instance=RequestContext(request))