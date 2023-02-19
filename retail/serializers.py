from rest_framework import serializers

from retail.models import Contractor, Retail, Seller


class ContractorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = '__all__'


class ContractorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = '__all__'


class ContractorCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Contractor
        exclude = ["retail_id", "trader_id"]

    def create(self, validated_data):
        contractor = Contractor.objects.create(**validated_data)
        contractor.save()
        return contractor


class ContractorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = ["id", "first_name", "last_name", "email", "phone"]

    def save(self):
        contractor = super().save()

        contractor.save()
        return contractor


class ContractorDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = ['id']


class RetailListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retail
        fields = '__all__'


class SellerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'
