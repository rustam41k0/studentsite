from django.urls import path

from mainapp.views import AllProjectsView, ProfileView, DetailProjectView, RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('', AllProjectsView.as_view(), name='all_projects'),
    path('project/<int:id>', DetailProjectView.as_view(), name='project'),
    path('profile/<int:id>', ProfileView.as_view(), name='profile'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

]
