from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Project, Profile


class AllProjectsView(ListView):
    model = Project
    template_name = 'all_projects.html'
    context_object_name = 'projects'


class DetailProjectView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    pk_url_kwarg = 'id'


class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'
    pk_url_kwarg = 'id'


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('all_projects')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('all_projects')


def logout_user(request):
    logout(request)
    return redirect('all_projects')
