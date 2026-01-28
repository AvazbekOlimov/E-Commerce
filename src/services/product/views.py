from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from services.product.models.product import Product
from services.product.serializers.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        price = self.request.query_params.get('price', None)
        if price is not None:
            return self.queryset.filter(price__lte=price)
        return self.queryset
    
    @action(detail=False, methods=['get'], url_path='under-price/(?P<price>[^/.]+)', url_name='under_price')
    def under_price(self, request, price=None):
        products = Product.objects.filter(price__lte=price)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

