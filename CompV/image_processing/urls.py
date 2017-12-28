from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /image_processing/
    url(r'^$', views.index, name='index'),
    # ex: /image_processing/upload_and_image_processing/
    url(r'^upload_and_image_processing/$', views.upload_and_image_processing, name='upload_and_image_processing'),
    # ex: /image_processing/datasets/
    url(r'^datasets/$', views.datasets, name='datasets'),
    url(r'^datasets/dataset_detail/$', views.dataset_detail, name='dataset_detail'),
    url(r'^registration/$', views.registration, name='registration'),
]