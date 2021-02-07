""" Models from posts """
from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
	""" POST model """
	
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

	title = models.CharField(max_length=250)
	photo = models.ImageField(upload_to = 'posts/photos')

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
