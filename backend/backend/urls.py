from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework import permissions
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path("api-auth/", include("rest_framework.urls", namespace="rest_frameworks")),
    # OpenAPI 3 documentation with Swagger UI
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(
            template_name="swagger.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
    path('swagger/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

# Customizing admin texts
admin.site.site_header = 'CodeJee by Pratap Educational Services PVT LTD.'
admin.site.index_title = 'Admin Dashboard'
admin.site.site_title = 'CodeJee'
