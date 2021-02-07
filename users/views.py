from django.contrib.auth import authenticate,login,logout 
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Profile

# Forms 
from users.forms import ProfileForm,SignupForm

# Create your views here.

def user_profile(request):
	""" User profile """
	profile = request.user.profile
	errores = False
	if request.method == 'POST':

		form = ProfileForm(request.POST,request.FILES)

		if form.is_valid():

			datos = form.cleaned_data
			
			profile.picture = datos["picture"]
			profile.website = datos["website"]
			profile.biography = datos["biography"]
			profile.phone_number = datos["phone_number"]
			profile.save()

			return redirect('update_profile')

	else:
		
		form = ProfileForm()



	context = {

		'profile': profile,
		'user': request.user,
		'form':form,
		'errores':errores
	}

	return render(request,'users/update_profile.html',context)


def users_login(request):

	""" Users Login """

	if(request.method == "POST"):

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request,username=username,password = password)

		if (user is not None):
			login(request, user)
			return redirect('posts:feed')
		else:
			return render(request,'users/login.html',{'error':'Invalid Username or password'})


	else:
		return render(request, 'users/login.html')


def users_logout(request):

	""" Users Logout """
	logout(request)
	return redirect('users:login')


def user_signup(request):
	""" Users Signin """
	if (request.method == 'POST'):
		form = SignupForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('users:login')
	else:
		form = SignupForm()


	return render(

		request=request,
		template_name='users/signup.html',
		context ={'form':form}
		
		)

def user_test_signup(request):

	return render(request, 'users/signup_test.html')



















