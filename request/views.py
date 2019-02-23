from django.shortcuts import render, Http404
from rest_framework import generics

from django.contrib.auth import get_user_model

from .serializers import (
	UserCreateSerializer,
)

def home(request):
	username_is = ""
	email_is = ""
	if request.user.is_authenticated:
		username_is = request.user
		email_is = request.user.email
	else:
		username_is = "unknown"
	template = 'index.html'
	context = {'name' : username_is,
			   'email' : email_is}
	return render(request, template, context)


User = get_user_model()

class AddUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer