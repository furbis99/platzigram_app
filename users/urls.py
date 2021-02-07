""" Users Urls """

# Django
from django.urls import path

# Views
from users import views

urlpatterns =[
	
	path(
		route='login/',
		view=views.users_login,
		name='login'
		),

	path(
		route='logout/',
		view=views.users_logout,
		name='logout'
		),

	path(
		route='signup/',
		view=views.user_signup,
		name='signup'
		),

	path(
		route='me/profile/',
		view=views.user_profile,
		name='update_profile'
		),
]