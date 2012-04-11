from django.conf.urls import patterns, include, url

from myapp.views import IndexPage

urlpatterns = patterns('',
    url(r'^$', view=IndexPage.as_view(), name="index"),
)
