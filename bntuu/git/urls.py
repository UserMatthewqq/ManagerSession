from django.urls import path

from .views import index, save_upload_file, load_data, delete_file

urlpatterns = [
    path('', index),
    path('save_files_url/', save_upload_file, name='save_upload_image'),
    path('load_files_url/', load_data, name='load_data'),
    path('delete_file/', delete_file, name='delete_file'),
]
