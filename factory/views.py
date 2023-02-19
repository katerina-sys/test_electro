import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from factory.models import Factory, Products
from factory.serializers import *


class FactoryListView(ListAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactoryListSerializer

    def get(self, request, *args, **kwargs):
        factory_city = request.GET.get('city', None)
        if factory_city:
            self.queryset = self.queryset.filter(
                city__icontains=factory_city
            )
        return super().get(request, *args, **kwargs)


class FactoryDetailView(RetrieveAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactoryDetailSerializer


class FactoryCreateView(CreateAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactoryCreateSerializer


class FactoryUpdateView(UpdateAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactoryUpdateSerializer


class FactoryDeleteView(DestroyAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactoryDeleteSerializer


class ProductsListView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsListSerializer
