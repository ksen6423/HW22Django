from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls", namespace="catalog")),
    path("", include("openpage.urls", namespace="openpage")),
    path("clientbase/", include("clientbase.urls", namespace="clientbase"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
