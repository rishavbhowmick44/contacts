from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('contactlist.urls')),
    path('admin/', admin.site.urls),
]
