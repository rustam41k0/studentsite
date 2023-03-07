from django.views.generic import ListView, DetailView

from .models import Project, Profile


class AllProjectsView(ListView):
    model = Project
    template_name = 'all_projects.html'


class DetailProjectView(DetailView):
    model = Project
    template_name = 'project_detail.html'


class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'
