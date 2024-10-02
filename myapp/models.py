from sre_constants import CATEGORY
from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.shortcuts import render
from django.utils import timezone
from pydantic import ValidationError



class UserProfile(AbstractUser):
    # Add any additional fields you need here
    age = models.PositiveIntegerField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)  # Nullable email field
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profiles',  # Custom related name to avoid clashes
        related_query_name='user_profile',
        blank=True,
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profiles',  # Custom related name to avoid clashes
        related_query_name='user_profile',
        blank=True,
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='productimages/')
    is_active = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    reorderlevel = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    
   

    def is_at_reorder_level(self):
        return self.quantity == self.reorderlevel

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Cart for {self.user.username}: {self.product.name}"
    

class Order(models.Model):
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('out_for_delivery', 'Out for Delivery'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    fullname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.fullname} placed on {self.created_at}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in order {self.order.id}"
# Create your models here.

# supplier.py
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_website = models.URLField(max_length=200)
    
    def _str_(self):
        return f"{self.pk} : {self.company_name}"
    


# models.py
class Supplier_order(models.Model):
    STATUS_CHOICES = [
        ('can be satisfied', 'Out for Delivery'),
        ('stock not available', 'Out of stock'),
    ]
    
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date_of_order = models.DateField(default=timezone.now)
    delivery_date = models.DateField()
    date_of_delivery = models.DateField(null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='no response')

#models.py for track the deit
from django.db import models
from django.contrib.auth.models import User

class HealthRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to user
    date = models.DateField(auto_now_add=True)  # Automatically add the entry date
    exercise_done = models.CharField(max_length=255)  # Description of exercises
    food_intake = models.TextField()  # Description of food intake
    calories_consumed = models.FloatField()  # Total calories consumed in a day
    calories_burned = models.FloatField()  # Total calories burned through exercise
    weight_target = models.FloatField()  # Weight target the user wants to achieve
    current_weight = models.FloatField()  # Current weight of the user

    def __str__(self):
        return f"{self.user.username} - {self.date}"

 #weekly checking
# models.py
from django.db import models

from django.db import models
class WeightTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    start_weight = models.FloatField()
    end_weight = models.FloatField()

    def weight_difference(self):
        """Calculate the weight difference between start and end weights."""
        return self.end_weight - self.start_weight

    def clean(self):
        """Optional: Ensure that start_date is before end_date."""
        if self.start_date > self.end_date:
            raise ValidationError("End date must be after start date.")

    def __str__(self):
        """Improve string representation to include meaningful info."""
        return f"Weight tracking from {self.start_date} to {self.end_date}: {self.start_weight}kg -> {self.end_weight}kg (Difference: {self.weight_difference()}kg)"