from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from api.models import Product, Stock
from api.serializers import ProductSerializer, StockSerializer
from rest_framework.filters import OrderingFilter


class CustomPaginators(LimitOffsetPagination):
    max_limit = 5
    limit_query_param = 'my_limit'
    offset_query_param = 'my_offset'


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPaginators
    filter_backends = [OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['title']
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = 'id'
    pagination_class = CustomPaginators
    search_fields = [
        'products__id', 'products__title', 'products__description'
    ]
