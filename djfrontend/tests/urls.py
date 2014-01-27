from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="djfrontend/base.html")),
)

urlpatterns += staticfiles_urlpatterns()