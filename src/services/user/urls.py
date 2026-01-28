from django.urls import path, include  # This fixes 'NameError'
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

# Ensure this is spelled exactly 'urlpatterns' (plural)
urlpatterns = [
    path('', include(router.urls)),
]