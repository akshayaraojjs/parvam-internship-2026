from django.urls import path
from .views import (
    ParkingSlotListCreate,
    ParkingSlotDetailUpdateDelete,
    CarParkingListCreate,
    CarParkingDetailUpdateDelete,
    CarParkingCheckoutView,
)

urlpatterns = [
    # Single Route used for 
    # Listing & Creating the Parking Slots
    path('slots/', ParkingSlotListCreate.as_view(), name='slot_list_create'),
    # Single View, Updating & Deleting the Parking Slots
    path('slots/<int:pk>/', ParkingSlotDetailUpdateDelete.as_view(), name='slot_detail'),

    # Listing & Parking the Cars
    path('parking/', CarParkingListCreate.as_view(), name='car_parking_list_create'),
    # Single Car Parking Details, Update & Delete the Cars Parked
    path('parking/<int:pk>/', CarParkingDetailUpdateDelete.as_view(), name='car_parking_detail'),
    
    # Checkout the Parked Cars
    path('parking/<int:pk>/checkout/', CarParkingCheckoutView.as_view(), name='car_parking_checkout'),
]