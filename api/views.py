from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from config.models import Buyer, Car, Purchase, Survey
from .serializers import BuyerSerializer, CarSerializer, PurchaseSerializer, SurveySerializer
from django.shortcuts import get_object_or_404

# --- Buyer Views ---

class BuyerListCreateView(APIView):
    def get(self, request):
        buyers = Buyer.objects.all()
        serializer = BuyerSerializer(buyers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BuyerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BuyerDetailView(APIView):
    def get(self, request, pk):
        buyer = get_object_or_404(Buyer, pk=pk)
        serializer = BuyerSerializer(buyer)
        return Response(serializer.data)

    def put(self, request, pk):
        buyer = get_object_or_404(Buyer, pk=pk)
        serializer = BuyerSerializer(buyer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        buyer = get_object_or_404(Buyer, pk=pk)
        serializer = BuyerSerializer(buyer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        buyer = get_object_or_404(Buyer, pk=pk)
        buyer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --- Car Views ---

class CarListCreateView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarDetailView(APIView):
    def get(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def put(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        serializer = CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --- Purchase Views ---

class PurchaseListCreateView(APIView):
    def get(self, request):
        purchases = Purchase.objects.all()
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PurchaseDetailView(APIView):
    def get(self, request, pk):
        purchase = get_object_or_404(Purchase, pk=pk)
        serializer = PurchaseSerializer(purchase)
        return Response(serializer.data)

    def put(self, request, pk):
        purchase = get_object_or_404(Purchase, pk=pk)
        serializer = PurchaseSerializer(purchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        purchase = get_object_or_404(Purchase, pk=pk)
        serializer = PurchaseSerializer(purchase, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        purchase = get_object_or_404(Purchase, pk=pk)
        purchase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --- Survey Views ---

class SurveyListCreateView(APIView):
    def get(self, request):
        surveys = Survey.objects.all()
        serializer = SurveySerializer(surveys, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SurveyDetailView(APIView):
    def get(self, request, pk):
        survey = get_object_or_404(Survey, pk=pk)
        serializer = SurveySerializer(survey)
        return Response(serializer.data)

    def put(self, request, pk):
        survey = get_object_or_404(Survey, pk=pk)
        serializer = SurveySerializer(survey, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        survey = get_object_or_404(Survey, pk=pk)
        serializer = SurveySerializer(survey, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        survey = get_object_or_404(Survey, pk=pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
