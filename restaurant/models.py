from django.db import models


class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()
    Created_at = models.DateTimeField(auto_now_add=True)
    Last_modified = models.DateTimeField(auto_now=True)
    
    def  __str__(self):
        return self.Title
    
    
    
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    NoOfGuest = models.IntegerField()
    BookingDate = models.DateTimeField()
    Created_at = models.DateTimeField(auto_now_add=True)
    Last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.Name
    
