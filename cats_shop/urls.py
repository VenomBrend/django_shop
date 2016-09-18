from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.CatsList.as_view(), name='index'),
    url(r'^cat/(?P<pk>[0-9]+)', views.CatDetail.as_view(), name='cat'),
    ]