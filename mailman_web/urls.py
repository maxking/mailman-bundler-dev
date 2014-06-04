from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

# Comment the next two lines to disable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url=reverse_lazy('hyperkitty.views.index.index'))),
    url(r'^$', 'postorius.views.list_index'),
    url(r'^mailman3/', include('postorius.urls')),
    url(r'^archives/', include('hyperkitty.urls')),
    url(r'', include('social_auth.urls')),
)
