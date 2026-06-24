from django.db import models
from django.utils import timezone

# Create your models here.
CAR_TYPE_CHOICES = [
    ('small', 'Small'),
    ('medium', 'Medium'),
    ('large', 'Large'),
]

# We have 2 models:
# ParkingSlot & CarParking
class ParkingSlot(models.Model):
    slot_number = models.CharField(max_length=10, unique=True)
    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        # True if(condition) else False
        status = "Booked" if self.is_booked else "Available"
        return f"Slot {self.slot_number} | {self.get_car_type_display()} | Rs.{self.hourly_rate}/hr | {status}"

class CarParking(models.Model):
    car_brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_number = models.CharField(max_length=20, unique=True)
    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)
    incoming_time = models.DateTimeField(auto_now_add=True)
    outgoing_time = models.DateTimeField(null=True, blank=True)
    parking_slot = models.ForeignKey(
        ParkingSlot, on_delete=models.PROTECT, related_name='sessions', 
        null=True, blank=True
    )
    amount_charged = models.DecimalField(max_digits=10, decimal_places=2, 
                                         null=True, blank=True)
    
    class Status(models.TextChoices):
        PARKED = 'parked', 'Parked'
        EXITED = 'exited', 'Exited'

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PARKED)

# Check this block later
    def __str__(self):
        return f"{self.car_number} -> Slot {self.parking_slot.slot_number if self.parking_slot else 'N/A'}"
    
    # 
    def calculate_charge(self):
        # Car Parking is not yet done, then Charges will be 0
        if not self.incoming_time or not self.parking_slot:
            return None
        end = self.outgoing_time or timezone.now()
        # 12:30 - 11:20 : 70mins
        elapsed_minutes = (end - self.incoming_time).total_seconds() / 60
        billable_hours = elapsed_minutes
        return round(billable_hours * float(self.parking_slot.hourly_rate), 2)