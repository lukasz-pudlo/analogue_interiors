from django.urls import path
from projects.views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='detail'),
    path('project/new/', ProjectCreateView.as_view(), name='new'),
    path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='edit'),
    path('project/<int:pk>/delete/',
         ProjectDeleteView.as_view(), name='delete')
]
