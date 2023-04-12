from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='home'),
    path('success', views.success, name='success'),
    path('preview', views.preview, name='preview'),
    path('nullsum', views.NullSum, name='nullsum'),
]