from django.conf.urls import patterns, include, url
from django.contrib import admin
from quickstart import views
from ui import views as ui_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
    url(r'^$', ui_views.index),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
