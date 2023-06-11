from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from projects.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'projects/project_form.html'
    fields = ['name', 'description']


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/project_form.html'
    fields = ['name', 'description']


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('projects:list')
