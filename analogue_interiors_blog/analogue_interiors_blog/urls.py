from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include(('projects.urls', 'projects'), namespace='projects'))
]
