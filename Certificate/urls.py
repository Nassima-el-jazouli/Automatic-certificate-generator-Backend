from django.contrib import admin
from django.urls import re_path
from Certificate import views

urlpatterns = [
    re_path(r'^certificates', views.Certificate_list),
    re_path(r'^create', views.certificate_create)

]