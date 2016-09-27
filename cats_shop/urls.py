from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.CatsList.as_view(), name='index'),
    url(r'^cat/(?P<pk>[0-9]+)', views.CatDetail.as_view(), name='cat'),
    url(r'^checkout/$', views.OrderAddView.as_view(), name='order'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    ]
