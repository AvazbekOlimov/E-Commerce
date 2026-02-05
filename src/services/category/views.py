from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions
from services.category.models.category import Category
from services.category.serializers.serializers import CategorySerializer
from services.user.permissions import IsAdminUser, IsVendorUser

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        
        return [permissions.IsAuthenticated(), (IsAdminUser | IsVendorUser)()]