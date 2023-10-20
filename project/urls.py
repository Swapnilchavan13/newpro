
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.views import *
from django.conf import settings
from django.conf.urls.static import static


# create the router and register
router = routers.DefaultRouter()


# create the router and register
router.register('image', ImageViewSet, basename='image')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
