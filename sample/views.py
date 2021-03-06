from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from datetime import datetime
from .forms import ProfileForm, ContactForm, UserRegForm, BulletinForm
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.mail import send_mail
from sample.models import Bulletin, User_profile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request, bulletin_id=1, profile_id=3, page_num=1):
	bulletins = Bulletin.objects.all()
	bulletins = Paginator(bulletins,3)
	context={
		'bulletin': Bulletin.objects.get(id=bulletin_id),
		'bulletins': bulletins.page(page_num),
		'persons': User_profile.objects.all(),
		'person': User_profile.objects.get(user_id=profile_id),

	}
	return(render(request,"bulletins.html",context))

def get_profile(request, profile_id = 1):
	fa = User_profile.objects.get(user_id=profile_id).user_country+' '+User_profile.objects.get(user_id=profile_id).user_adress
	context={
		'person': User_profile.objects.get(user_id=profile_id),
		'person_f_a': fa,
		'users': User_profile.objects.all(),
	}
	return(render(request,"profile.html",context))

def contact(request):
	form = ContactForm(request.POST)
	context={'form': form}
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email , 'youothermail@mail.com']
		contact_message = "%s: %s via %s"%(
			form_full_name,
			form_message, 
			form_email)

		send_mail(subject,
			contact_message,
			from_email, 
			to_email, 
			fail_silently = True)
	return(render(request,"contact.html",context))

def add_bulletin(request):
	form = BulletinForm(request.POST)
	context = {
	'form': form,
	}
	return(render(request,"bulletin_form.html",context))

def get_bulletin(request):
	if request.POST:
		data = Bulletin(user = request.user)
		form = BulletinForm(request.POST)
		if form.is_valid():
			data.text = form.cleaned_data.get("bulletin_text")
			data.title = form.cleaned_data.get("bulletin_title")
			data.user = request.user
			data.date = datetime.today() 
			data.save()
		else:
			return redirect('bulletin_form.html')
	return redirect('/')