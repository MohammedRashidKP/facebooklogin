from django.shortcuts import render
from django.http import HttpResponse
from social_django.models import UserSocialAuth
from .models import Greeting

# Create your views here.
from django.contrib.auth.decorators import login_required


def index(request):
    #return HttpResponse('Hello from Python!')
    return render(request, 'base.html')


def db(request):
	return render(request, 'index.html')
	
def facebook(request):	
	user = request.user
	try:
		facebook_login = user.social_auth.get(provider='facebook')
	except UserSocialAuth.DoesNotExist:
		return HttpResponse('Hello from Python!')
	return HttpResponse('Hello from Python!adas')
		