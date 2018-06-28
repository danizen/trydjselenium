from django.conf.urls import include, url
from django.conf import settings
from djsel import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='home'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [ url(r'__debug__/', include(debug_toolbar.urls)), ]
