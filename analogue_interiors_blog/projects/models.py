from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})
