# Import the necessary admin components from Django and the models to be registered
from django.contrib import admin
from .models import Order, OrderLineItem

# Define an inline admin class to manage OrderLineItems within the Order admin interface
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem  # Specify the model to be displayed inline (OrderLineItem)
    readonly_fields = ('lineitem_total',)  # Make the 'lineitem_total' field read-only in the admin interface

# Define the admin class for the Order model
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)  # Display OrderLineItem as an inline (embedded form) in the Order admin

    # Specify which fields should be read-only in the admin interface
    readonly_fields = ('order_number', 'date', 
                       'delivery_cost', 'order_total', 
                       'grand_total',)

    # Define the order and grouping of fields in the admin detail view
    fields = ('order_number', 'date', 'full_name', 
              'email', 'phone_number', 'country', 
              'postcode', 'town_or_city', 'street_address1', 
              'street_address2', 'county', 'delivery_cost', 
              'order_total', 'grand_total',)

    # Specify which fields will be displayed in the list view (summary of orders)
    list_display = ('order_number', 'date', 'full_name', 
                    'order_total', 'delivery_cost', 
                    'grand_total',)

    # Set the default ordering of the orders by date in descending order
    ordering = ('-date',)

# Register the Order model with the custom OrderAdmin configuration
admin.site.register(Order, OrderAdmin)
