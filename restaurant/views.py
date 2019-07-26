from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


class CustomPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        from django.db import connection
        from ChakhLe_BE.variables import CUISINES

        cursor = connection.cursor()
        cursor.execute('''select count(*) from restaurant_restaurant
                       where addtime(current_time, '05:30') between open_from and open_till''')

        row = cursor.fetchone()
        open_restaurants = row[0]
        cuisines = []

        for i in CUISINES:
            cuisines.append(i[1])

        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            "open_restaurants": open_restaurants,
            "cuisines": cuisines,
            'results': data,
        })


class RestaurantListView(ListCreateAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter
    from django_filters.rest_framework.backends import DjangoFilterBackend

    from .serializers import RestaurantSerializer
    from .models import Restaurant

    permission_classes = (AllowAny, )
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, )
    filter_fields = ('id', 'name', 'commission', 'is_veg')
    search_fields = ('name', 'id')
    ordering = ['-discount']


class RetrieveRestaurantView(RetrieveUpdateAPIView):
    from rest_framework.permissions import AllowAny

    from .models import Restaurant
    from .serializers import RestaurantSerializer

    permission_classes = (AllowAny, )
    queryset = Restaurant.objects.filter(is_active=True)
    serializer_class = RestaurantSerializer


class RestaurantImageListView(ListCreateAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter

    from .serializers import RestaurantImageSerializer
    from .models import RestaurantImage

    permission_classes = (AllowAny, )
    serializer_class = RestaurantImageSerializer
    queryset = RestaurantImage.objects.all()

    filter_backends = (SearchFilter, )
    search_fields = ('id', 'name')
