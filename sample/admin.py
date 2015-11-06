from django.contrib import admin
from sample.models import Bulletin, User_profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
	model = User_profile

class UserProfileAdmin(UserAdmin):
	inlines = [ UserProfileInline, ]

# Register your models here.
class BulletinAdmin(admin.ModelAdmin):
	fields = ('title','text','user','date')
	list_display = ('id','title')

admin.site.register(Bulletin, BulletinAdmin)
admin.site.register(User, UserProfileAdmin)