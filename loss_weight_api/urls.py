from django.conf.urls import include, patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from loss_weight_api import views

urlpatterns = patterns('',
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),
    url(r'^checkpoints/$', views.CheckPointList.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)