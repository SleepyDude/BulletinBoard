from django import forms
from registration.forms import RegistrationForm
from django.forms import ModelForm
from sample.models import User_profile
from django.forms.extras.widgets import SelectDateWidget
import datetime

class ProfileForm(forms.Form):
	your_login = forms.CharField(label = 'Login:',max_length=100)
	your_email = forms.EmailField(label = 'E-mail:')

class ContactForm(forms.Form):
	email = forms.EmailField(label="Your E-mail")
	message = forms.CharField()
	full_name = forms.CharField()

class UserRegForm(RegistrationForm):
	full_name = forms.CharField(max_length = 30)
	# birthday = forms.DateField(widget = SelectDateWidget(years=range(1936, datetime.date.today().year)))
	birthday = forms.DateField(label='birthday YYYY-MM-DD')
	user_adress = forms.CharField(max_length = 35)
	user_city = forms.CharField(max_length = 20)
	user_state = forms.CharField(max_length = 20)
	user_country = forms.CharField(max_length = 20)
	user_zip = forms.IntegerField()


class BulletinForm(forms.Form):
	bulletin_title = forms.CharField(max_length = 30)
	bulletin_text = forms.CharField()