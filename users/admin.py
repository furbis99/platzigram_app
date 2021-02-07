from django.contrib import admin
# Register your models here.
from users.models import Profile

@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):

	list_display = ('pk','user','website','phone_number','biography','picture')

	list_display_links = ('pk','user')

	list_editable = ('phone_number','biography','picture')

	search_fields = (
		'user__email',
		'user__username',
		'user__firstname',
		'phone_number')


	
