from django.contrib import admin
from profiles_api.models import User_Profile,snippet,ProfileFeedItem
# Register your models here.


admin.site.register(User_Profile)
admin.site.register(snippet)
admin.site.register(ProfileFeedItem)