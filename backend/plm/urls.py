from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('api/v1/', include('parts.urls')),
    path('admin/', admin.site.urls),
]

