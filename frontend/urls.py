# frontend/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('frontend/', include('frontend.urls')),
    path('admin/', admin.site.urls),
]
