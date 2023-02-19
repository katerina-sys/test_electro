from rest_framework import serializers

from factory.models import Factory, Products


class FactoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'


class FactoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'


class FactoryCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Factory
        exclude = ["street", "house_number", "debt"]

    def create(self, validated_data):
        factory = Factory.objects.create(**validated_data)
        factory.save()
        return factory


class FactoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ["id", "title", "country", "city"]

    def save(self):
        factory = super().save()

        factory.save()
        return factory


class FactoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ['id']


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
