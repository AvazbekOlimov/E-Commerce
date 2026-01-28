
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce API",
        default_version='v1',
        description="Online shop backend API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/category/', include('services.category.urls')), # Suggested: add prefix
    path('api/product/', include('services.product.urls')),
    path('api/user/', include('services.user.urls')),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
]