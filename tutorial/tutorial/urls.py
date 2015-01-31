from django.conf.urls import patterns, include, url
from django.contrib import admin
from quickstart import views
from ui import views as ui_views
from restfulAPI import views as restful_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tables', restful_views.TableViewSet)
router.register(r'meals', restful_views.MealViewSet)

urlpatterns = patterns('',
    url(r'^$', ui_views.index),
    url(r'^api/', include(router.urls)),
    #url(r'^api/', restful_views),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
