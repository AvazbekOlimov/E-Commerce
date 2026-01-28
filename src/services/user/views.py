from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated
from services.user.serializers.user import UserSerializer
from services.user.models.user import User
from services.user.permissions import IsAdminUser, IsVendorUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    
    
    # Your existing by_role action
    @action(detail=False, methods=['get'], url_path='by-role/(?P<role>[^/.]+)', url_name='by_role')
    def by_role(self, request, role=None):
        users = self.queryset.filter(role=role)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        role = self.request.query_params.get('role', None)
        if role is not None:
            return self.queryset.filter(role=role)
        return self.queryset
    
    def get_permissions(self):
        if self.action == 'register':
            return [permissions.AllowAny()]
        if self.action == 'list':
            # Only Admins can see the list of all users
            return [IsAdminUser()]
        return [permissions.IsAuthenticated()]