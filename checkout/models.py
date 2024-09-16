# Import necessary libraries and models
import uuid  # Used to generate unique order numbers
from django.db import models  # Provides access to Django's model system
from django.db.models import Sum  # Used to calculate the sum of line items
from django.conf import settings  # Access to project settings

from products.models import Product  # Import the Product model from the products app

# Define the Order model
class Order(models.Model):
    # Basic order information fields
    order_number = models.CharField(max_length=32, null=False, editable=False)  # Unique order number, not editable
    full_name = models.CharField(max_length=50, null=False, blank=False)  # Full name of the customer
    email = models.EmailField(max_length=254, null=False, blank=False)  # Customer email address
    phone_number = models.CharField(max_length=20, null=False, blank=False)  # Customer phone number
    country = models.CharField(max_length=40, null=False, blank=False)  # Customer's country
    postcode = models.CharField(max_length=20, null=True, blank=True)  # Postal code, optional field
    town_or_city = models.CharField(max_length=40, null=False, blank=False)  # Customer's town or city
    street_address1 = models.CharField(max_length=80, null=False, blank=False)  # Primary street address
    street_address2 = models.CharField(max_length=80, null=True, blank=True)  # Secondary street address (optional)
    county = models.CharField(max_length=80, null=True, blank=True)  # County or region (optional)
    date = models.DateTimeField(auto_now_add=True)  # Date the order was created, automatically set
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)  # Cost of delivery
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)  # Total cost of the order (excluding delivery)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)  # Total cost of the order (including delivery)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID.
        UUID ensures uniqueness for every order.
        """
        return uuid.uuid4().hex.upper()  # Generate a random order number

    def update_total(self):
        """
        Update the grand total each time a line item is added or modified.
        This method calculates the order total and adjusts for delivery costs.
        """
        # Calculate the total of all line items
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']or 0
        
        # Determine delivery cost based on whether the total is below the free delivery threshold
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100  # Standard delivery cost
        else:
            self.delivery_cost = 0  # Free delivery
        
        # Calculate the grand total (order total + delivery cost)
        self.grand_total = self.order_total + self.delivery_cost
        
        # Save the updated order totals
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already before saving the order.
        """
        # Check if the order number has already been set
        if not self.order_number:
            # Generate an order number if not already present
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)  # Call the original save method

    def __str__(self):
        """
        Return the string representation of the order, which is the order number.
        """
        return self.order_number


# Define the OrderLineItem model
class OrderLineItem(models.Model):
    # ForeignKey to associate each line item with an order
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)  # Link to the ordered product
    product_size = models.CharField(max_length=2, null=True, blank=True)  # Optional size of the product (XS, S, M, L, XL)
    quantity = models.IntegerField(null=False, blank=False, default=0)  # Quantity of this product in the order
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)  # Total cost for this line item

    def save(self, *args, **kwargs):
        """
        Override the original save method to calculate the line item total
        and update the overall order total.
        """
        # Calculate the total for this line item (product price * quantity)
        self.lineitem_total = self.product.price * self.quantity
        
        # Call the original save method to store the line item in the database
        super().save(*args, **kwargs)

        # After saving, update the total of the associated order
        self.order.update_total()

    def __str__(self):
        """
        Return the string representation of the line item,
        showing the product SKU and the order number it belongs to.
        """
        return f'SKU {self.product.sku} on order {self.order.order_number}'
