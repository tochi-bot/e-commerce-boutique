# Import necessary signal components from Django
from django.db.models.signals import post_save, post_delete  # Signals that trigger after saving or deleting an object
from django.dispatch import receiver  # Decorator to register a function as a signal receiver

# Import the OrderLineItem model
from .models import OrderLineItem

# Define a function to be triggered after a line item is saved or updated
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update the order total whenever a line item is created or updated.
    'instance' refers to the specific OrderLineItem instance being saved,
    and it will trigger the update_total method on the associated order.
    """
    instance.order.update_total()  # Call the update_total method to recalculate the order's total

# Define a function to be triggered after a line item is deleted
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update the order total whenever a line item is deleted.
    This ensures that the order total reflects the removal of the line item.
    """
    instance.order.update_total()  # Call the update_total method to recalculate the order's total after deletion
