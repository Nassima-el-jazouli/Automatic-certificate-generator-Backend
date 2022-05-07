from django.conf import settings
from django.contrib import admin
from django.urls import re_path
from django.conf.urls import include
from django.conf.urls.static import static

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^', include('Certificate.urls')),
]



if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)