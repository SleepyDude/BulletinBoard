from sample.models import User_profile
from .forms import UserRegForm

def user_created(sender, request, user, **kwargs):
	form = UserRegForm(request.POST)
	data = User_profile(user=user)
	print(data.full_name)
	data.full_name = request.POST["full_name"]
	data.birthday = request.POST["birthday"]
	data.user_adress = request.POST["user_adress"]
	data.user_city = request.POST["user_city"]
	data.user_state = request.POST["user_state"]
	data.user_country = request.POST["user_country"]
	data.user_zip = request.POST["user_zip"]
	data.save()


from registration.signals import user_registered
user_registered.connect(user_created)