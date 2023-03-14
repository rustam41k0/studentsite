from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # context['user_projects'] = Profile.objects.filter(author__user_id=)
        return context
