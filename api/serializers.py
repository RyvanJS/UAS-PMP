from rest_framework import serializers
from config.models import Buyer, Car, Purchase, Survey


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    buyer = BuyerSerializer(read_only=True)
    car = CarSerializer(read_only=True)
    buyer_id = serializers.PrimaryKeyRelatedField(queryset=Buyer.objects.all(), write_only=True, source='buyer')
    car_id = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), write_only=True, source='car')

    class Meta:
        model = Purchase
        fields = ['id', 'buyer', 'car', 'buyer_id', 'car_id', 'date', 'payment_method']


class SurveySerializer(serializers.ModelSerializer):
    purchase = PurchaseSerializer(read_only=True)
    purchase_id = serializers.PrimaryKeyRelatedField(queryset=Purchase.objects.all(), write_only=True, source='purchase')

    class Meta:
        model = Survey
        fields = ['id', 'purchase', 'purchase_id', 'satisfaction_rating', 'comments', 'would_recommend', 'created_at']
