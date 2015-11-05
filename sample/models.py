from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bulletin(models.Model):
	class Meta:
		db_table = "bulletin"
	title = models.CharField(max_length=30)
	text = models.TextField()
	date = models.DateField()

class User_profile(models.Model):
	class Meta:
		db_table = 'profile'
	user = models.ForeignKey(User, unique = True)
	full_name = models.CharField(max_length = 30)
	birthday = models.DateField()
	user_adress = models.CharField(max_length = 35)
	user_city = models.CharField(max_length = 20)
	user_state = models.CharField(max_length = 20)
	user_country = models.CharField(max_length = 20)
	user_zip = models.IntegerField(null=True)
