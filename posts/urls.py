""" Posts Urls """

#Django
from django.urls import path

#Views 
from posts import views

# Managment urls
urlpatterns=[
	
	path(
		route='',
		view=views.lis_post,
		name='feed'
		),

	path(
		route='posts/new',
		view=views.new_post,
		name='create'
		)
]