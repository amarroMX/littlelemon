from rest_framework.serializers import ModelSerializer
from .models import Menu, Booking


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ["Title","Price","Inventory"]
        
class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ["Name","NoOfGuest"]
        read_only_fields = ["BookingDate"]