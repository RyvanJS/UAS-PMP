from django.urls import path
from .views import (
    BuyerListCreateView, BuyerDetailView,
    CarListCreateView, CarDetailView,
    PurchaseListCreateView, PurchaseDetailView,
    SurveyListCreateView, SurveyDetailView,
)

urlpatterns = [
    # Buyer
    path('buyers/', BuyerListCreateView.as_view(), name='buyer-list-create'),
    path('buyers/<int:pk>/', BuyerDetailView.as_view(), name='buyer-detail'),

    # Car
    path('cars/', CarListCreateView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),

    # Purchase
    path('purchases/', PurchaseListCreateView.as_view(), name='purchase-list-create'),
    path('purchases/<int:pk>/', PurchaseDetailView.as_view(), name='purchase-detail'),

    # Survey
    path('surveys/', SurveyListCreateView.as_view(), name='survey-list-create'),
    path('surveys/<int:pk>/', SurveyDetailView.as_view(), name='survey-detail'),
]
