from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('videoconference_app.urls')),
    path('', include('board.urls')),
    path('', include('git.urls')),
]
