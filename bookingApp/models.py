from django.db import models

class Booking(models.Model):
    service_name = models.TextField()
    date = models.DateField()
    time_slot = models.TimeField()

    def __str__(self):
        return f"Booking by {self.user.email} for {self.service_name} on {self.date} at {self.time_slot}"