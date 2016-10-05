from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from django_shop import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cats_shop.urls', namespace='cats_shop',
                      app_name="cats_shop")),
    url(r'^cart/', include('cart.urls', namespace='cart', app_name='cart')),
    url(r'^profile/(?P<pk>\d+)/$',
        login_required(views.UserProfileDetail.as_view()),
        name='profile'),
    url(r'^profile/(?P<pk>\d+)/update/$',
        login_required(views.UserProfileUpdate.as_view()),
        name='profile_edit')

    ] + static(
        settings.STATIC_URL
    ) + static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
