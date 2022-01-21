from django.contrib import admin
from django.urls import include, path, re_path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views
from rest_framework.permissions import AllowAny

from receipts.urls import router

schema_view = get_schema_view(
    openapi.Info(
        title="Receipt Generator API",
        default_version="v1",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("admin/", admin.site.urls),
    path("api-token-auth/", views.obtain_auth_token),
    path("", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
