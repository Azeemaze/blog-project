from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import DetailView

from app.models import Profile
from .forms import SignupForm,EditProfileForm,PasswordChangingForm,ProfilePageForm

# Create your views here.

class CreateProfilePage(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'app/create_profile_page.html'
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'app/edit_profile_page.html'
    fields = ['Bio','Profile_picture','website_url','facebook_url','instagram_url']
    success_url = reverse_lazy('home')
class ProfilePageView(DetailView):
    model = Profile
    template_name = 'app/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile,id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'app/password_success.html', {})
class UserRegisterView(generic.CreateView):
    form_class = SignupForm
    template_name = 'app/registration.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'app/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user