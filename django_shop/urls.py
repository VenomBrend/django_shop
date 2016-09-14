from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^shop/', include('cats_shop.urls', namespace="cats_shop")),
    url(r'^admin/', include(admin.site.urls)),
    ] + static(
        settings.STATIC_URL
    ) + static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )
