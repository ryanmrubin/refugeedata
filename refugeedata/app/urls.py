from django.conf import settings
from django.conf.urls import include, url, static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', 'refugeedata.views.home', name='public'),
]

urlpatterns += i18n_patterns(
    url(r'^$', RedirectView.as_view(pattern_name="public", permanent=True)),
    url(r'^registration/', include('refugeedata.registration.urls',
        app_name="registration", namespace="reg")),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
