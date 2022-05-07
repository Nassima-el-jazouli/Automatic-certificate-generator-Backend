from django.contrib import admin
from django.urls import re_path
from Certificate import views

urlpatterns = [
    re_path(r'^certificates$', views.view_certificates),
    re_path(r'^certificates$', views.create_certificate),
    re_path(r'^certificates$', views.delete_all),
    re_path(r'^certificates/(?P<pk>[0-9]+)$', views.update_certificate),
    re_path(r'^certificates/(?P<pk>[0-9]+)$', views.delete_certificate),
]