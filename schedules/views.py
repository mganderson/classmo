from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login


def index(request):
	##user=request.user gets user object
	return render(request,'schedules/index.html')

def register(request):
	username=request.POST.get('user','')
	password=request.POST.get('password','')
	email=request.POST.get('email','')
	fname=request.POST.get('fname','')
	lname=request.POST.get('lname','')
	user=User.objects.create_user(username,email,password)
	user.first_name=fname
	user.last_name=lname
	user.save()
	check = authenticate(request, username=username, password=password)
	if check is not None:
		login(request,user)
		return redirect('schedules:index')
	else:
		return HttpResponse("something badd happened")
