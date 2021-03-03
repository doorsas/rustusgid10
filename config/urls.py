from django.conf import settings
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Rustus Gidas"
admin.site.site_title = "Rustus Gidas Gi"
admin.site.index_title = "Rustus Gidas GID"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('oras/', include('oras.urls')),
    path('technikosnuoma/', include('technikosnuoma.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
