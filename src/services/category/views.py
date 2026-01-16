from rest_framework.viewsets import ModelViewSet
from services.category.models.models import Category
from services.category.serializers.serializers import CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'delete']