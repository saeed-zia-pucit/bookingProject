from django.db import models
from django.core.exceptions import ValidationError

class BusinessProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    start_time = models.TimeField()  # Business start time
    end_time = models.TimeField()    # Business end time

    def save(self, *args, **kwargs):
        if not self.pk and BusinessProfile.objects.exists():
            raise ValidationError('There can be only one BusinessProfile instance')
        return super(BusinessProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)  # Duration in minutes as a string

    def __str__(self):
        return f"{self.name} - {self.business.email}"
