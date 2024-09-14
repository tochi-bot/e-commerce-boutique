# Import the necessary AppConfig class from Django's apps module
from django.apps import AppConfig


# Define the configuration class for the 'checkout' app
class CheckoutConfig(AppConfig):
    # Set the name of the app
    name = 'checkout'

    # Override the ready method, which is called when the application is ready
    def ready(self):
        """
        Import the signals module when the Django app is ready.
        This ensures that the signal handlers (like those for updating order totals)
        are connected when the app starts.
        """
        import checkout.signals  # Import the signals to ensure they are registered
