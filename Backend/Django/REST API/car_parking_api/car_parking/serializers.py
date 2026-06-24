from rest_framework import serializers
from django.utils import timezone
from .models import ParkingSlot, CarParking

class ParkingSlotSerializer(serializers.ModelSerializer):
    car_type_display = serializers.CharField(source='get_car_type_display', read_only=True)

    class Meta:
        model = ParkingSlot
        # What we show to end-user
        fields = [
            'id',
            'slot_number',
            'car_type',
            'car_type_display',
            'hourly_rate',
            'is_booked',
        ]
        # Abstraction Layer to hide the unnecessary data from end-user
        readonlyfields = ['is_booked']

class CarParkingSerializer(serializers.ModelSerializer):
    slot_number = serializers.CharField(source='parking_slot.slot_number', read_only=True)
    hourly_rate = serializers.DecimalField(source='parking_slot.hourly_rate', max_digits=8, decimal_places=2, read_only=True)
    car_type_display = serializers.CharField(source='get_car_type_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    estimated_charge = serializers.SerializerMethodField()

    class Meta:
        model = CarParking
        fields = [
            'id',
            'car_brand',
            'car_model',
            'car_number',
            'car_type',
            'car_type_display',
            'parking_slot',
            'slot_number',
            'hourly_rate',
            'incoming_time',
            'outgoing_time',
            'status',
            'status_display',
            'amount_charged',
            'estimated_charge',
        ]    
        read_only_fields = [
            'incoming_time',
            'outgoing_time',
            'status',
            'amount_charged',
        ]

    # Helper method for calling the calculate_charge() method
    def get_estimated_charge(self, obj):
        if obj.status == CarParking.Status.PARKED:
            return obj.calculate_charge()
        return None
    
    # Check if parking slot already booked or is it available to park
    def validate_parking_slot(self, slot):
        if slot.is_booked:
            raise serializers.ValidationError(
                f"Slot '{slot.slot_number}' is already booked."
            )
        return slot
    
    # To match the slot with car type, only matching size will allocate for parking
    def validate(self, data):
        slot = data.get('parking_slot')
        car_type = data.get('car_type')
        if slot and car_type and slot.car_type != car_type:
            raise serializers.ValidationError(
                f"Slot '{slot.slot_number}' is designed for "
                f"'{slot.get_car_type_display()}' cars, not '{car_type}'."
            )
        return data
    
    # If everything is valid then allocate a requested Slot
    def create(self, validated_data):
        slot = validated_data['parking_slot']
        slot.is_booked = True
        slot.save()
        return super().create(validated_data)
    
class CarParkingCheckoutSerializer(serializers.ModelSerializer):
    slot_number = serializers.CharField(source='parking_slot.slot_number', read_only=True)
    car_type_display = serializers.CharField(source='get_car_type_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = CarParking
        fields = [
            'id',
            'car_brand',
            'car_model',
            'car_number',
            'car_type',
            'car_type_display',
            'slot_number',
            'incoming_time',
            'outgoing_time',
            'status',
            'status_display',
            'amount_charged',
        ]
        read_only_fields = fields

    # Checkout procedure to capture the outgoing time
    def update(self, instance, validate_data):
        if instance.status == CarParking.Status.EXITED:
            raise serializers.ValidationError("This car has already exited.")
        
        instance.outgoing_time = timezone.now()
        instance.status = CarParking.Status.EXITED
        instance.amount_charged = instance.calculate_charge()

        if instance.parking_slot:
            instance.parking_slot.is_booked = False
            instance.parking_slot.save()

        instance.save()
        return instance