from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

from retail.models import *
from retail.serializers import *


class ContractorListView(ListAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorListSerializer


class ContractorDetailView(RetrieveAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorDetailSerializer


class ContractorCreateView(CreateAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorCreateSerializer


class ContractorUpdateView(UpdateAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorUpdateSerializer


class ContractorDeleteView(DestroyAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorDeleteSerializer


class RetailListView(ListAPIView):
    queryset = Retail.objects.all()
    serializer_class = RetailListSerializer

    def get(self, request, *args, **kwargs):
        retail_city = request.GET.get('city', None)
        if retail_city:
            self.queryset = self.queryset.filter(
                city__icontains=retail_city
            )
        return super().get(request, *args, **kwargs)


class SellerListView(ListAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerListSerializer
