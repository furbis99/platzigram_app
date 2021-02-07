""" Post Forms """
# Django
from django.forms import ModelForm

#Models
from .models import Post


class PostForm(ModelForm):
	""" Post Model Form """
	
	class Meta:
		""" Setting model """

		model = Post
		fields = ['user','profile','title','photo']
		