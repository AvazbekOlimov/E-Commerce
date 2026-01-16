from rest_framework import viewsets
from services.product.models.models import Product
from services.product.serializers.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
# Create your views here.
