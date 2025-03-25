from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# Overriding AdminSite attributes.
admin.site.site_header = admin.site.site_title = "GYMNASTICA"

urlpatterns = [
    path("admin/", admin.site.urls),
]

# Include debug toolbar URLs.
if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()

# Include static URLs.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
