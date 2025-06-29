from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class EditProfileView(UpdateView, LoginRequiredMixin):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = '/task/list_task/'

    def get_object(self, queryset=None):
        return self.request.user.profile


class ShowProfileView(DetailView, LoginRequiredMixin):
    model = Profile
    template_name = 'registration/show_profile.html'
    context_object_name = 'profile'
    success_url = '/task/list_task/'

    def get_object(self, queryset=None):
        return self.request.user.profile
