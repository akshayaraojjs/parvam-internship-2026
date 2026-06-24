from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import ParkingSlot, CarParking
from .serializers import (
    ParkingSlotSerializer,
    CarParkingSerializer,
    CarParkingCheckoutSerializer,
)

class ParkingSlotListCreate(generics.ListCreateAPIView):
    serializer_class = ParkingSlotSerializer

    # GET (Fetch All Data), POST (To Add New Data)
    def get_queryset(self):
        qs = ParkingSlot.objects.all().order_by('slot_number')
        car_type = self.request.query_params.get('car_type')
        available = self.request.query_params.get('available')

        if car_type:
            qs = qs.filter(car_type=car_type)
        if available and available.lower() == 'true':
            qs = qs.filter(is_booked=False)
        return qs
    
    # GET - ID (View Data), PUT - ID(Update Data), DELETE - ID(Delete Data)
class ParkingSlotDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
        queryset = ParkingSlot.objects.all()
        serializer_class = ParkingSlotSerializer

class CarParkingListCreate(generics.ListCreateAPIView):
        serializer_class = CarParkingSerializer

        def get_queryset(self):
             qs = CarParking.objects.select_related('parking_slot').order_by('-incoming_time')
             sess_status = self.request.query_params.get('status')
             if sess_status:
                  qs = qs.filter(status=sess_status)
             return qs

class CarParkingDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
     queryset = CarParking.objects.select_related('parking_slot')
     serializer_class = CarParkingSerializer

class CarParkingCheckoutView(APIView):
     def post(self, request, pk):
        session = get_object_or_404(CarParking, pk=pk)
        serializer = CarParkingCheckoutSerializer(
            session, data={}, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
             {
                  "message": f"Car '{session.car_number}' has exited successfully.",
                  "session": serializer.data,
             },
             status=status.HTTP_200_OK,
        )
