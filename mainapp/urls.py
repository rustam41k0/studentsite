from django.urls import path

from mainapp.views import AllProjectsView, ProfileView, DetailProjectView

urlpatterns = [
    path('', AllProjectsView.as_view(), name='all_projects'),
    path('project/<int:id>', DetailProjectView.as_view(), name='project'),
    path('profile/<int:id>', ProfileView.as_view(), name='profile'),
]
