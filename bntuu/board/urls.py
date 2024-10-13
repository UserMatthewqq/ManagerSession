from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from .views import index, save_data, load_data, delete_item, save_upload_image, load_img, save_coord_img, delete_img

urlpatterns = [
    path('', index),
    path('.css', TemplateView.as_view(
            template_name='main.css',
            content_type='text/css')),
    path('save_data/', save_data, name='save_data'),
    path('load_data/', load_data, name='load_data'),
    path('delete_item/', delete_item, name='delete_item'),
    path('save_img_url/', save_upload_image, name='save_upload_image'),
    path('load_img/', load_img, name='load_img'),
    path('save_coord_img/', save_coord_img, name='save_coord_img'),
    path('delete_img/', delete_img, name='delete_img'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
