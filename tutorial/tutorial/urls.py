from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from quickstart import views
from ui import views as ui_views
from restfulAPI import views as restful_views
from rest_framework import routers
from django.conf.urls.static import static

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'tables', restful_views.TableViewSet)
router.register(r'meals', restful_views.MealViewSet)
router.register(r'locations', restful_views.LocationViewSet)
router.register(r'persons', restful_views.PersonViewSet)

urlpatterns = patterns('',
    url(r'^$', ui_views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^results$', ui_views.results),
    url(r'^api/', include(router.urls)),
    #url(r'^api/', restful_views),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
