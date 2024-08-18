from django.db import models

class Customer(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    ]
    

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')  
    name = models.CharField(max_length=255)  
    phone = models.CharField(max_length=20) 
    address = models.TextField()
    opening_amount = models.DecimalField(max_digits=10, decimal_places=2)  
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return self.name
