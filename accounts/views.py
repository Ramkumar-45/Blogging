from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .forms import UserForm, ProfileCreateFrom, ProfileEditView
from blogweb.models import ProfileUser, Post

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
# user registration
class UserRegisterView(CreateView):
    model = ProfileUser
    form_class = UserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


# specific user profile creation
@method_decorator(login_required, name='dispatch')  # -> used for only logged in user to access the page
class CreateProfileView(CreateView):
    model = ProfileUser
    form_class = ProfileCreateFrom
    template_name = 'registration/createprofile.html'

    def form_valid(self, form):  # validates a specific and instance user form
        form.instance.user = self.request.user
        return super().form_valid(form)


# specific user profile edit
@method_decorator(login_required, name='dispatch')  # -> used for only logged in user to access the page
class EditProfilePage(UpdateView):
    model = ProfileUser
    template_name = 'registration/edit_profile_page.html'
    fields = [
        'bio', 'profile_image', 'website_url', 'facebook_url', 'instagram_url', 'linkedIn_url'
    ]
    success_url = reverse_lazy('home')


# specific user general settings
@method_decorator(login_required, name='dispatch')  # -> used for only logged in user to access the page
class UserEditView(UpdateView):
    form_class = ProfileEditView
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


@method_decorator(login_required, name='dispatch')  # -> used for only logged in user to access the page
class ProfilePage(DetailView):
    model = ProfileUser
    template_name = 'registration/userprofile.html'

    def get_context_data(self, *args, **kwargs):  # returns a specific user data and their related posts
        users = ProfileUser.objects.all()
        context = super(ProfilePage, self).get_context_data(*args, **kwargs)
        specific_user = get_object_or_404(ProfileUser, id=self.kwargs['pk'])
        specific_user_post = Post.objects.filter(author=specific_user.id)
        context['userpage'] = specific_user
        context['userposts'] = specific_user_post
        return context


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('home')
