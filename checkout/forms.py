# Import necessary modules from Django
from django import forms  # Import the forms module for creating forms
from .models import Order  # Import the Order model to base the form on

# Define a form class for the Order model
class OrderForm(forms.ModelForm):
    # Meta class to specify the model and fields to include in the form
    class Meta:
        model = Order  # Use the Order model to create the form
        fields = ('full_name', 'email', 'phone_number',  # Specify fields to be included in the form
                  'street_address1', 'street_address2', 
                  'town_or_city', 'postcode', 'country', 
                  'county',)

    # Override the default form initialization method
    def __init__(self, *args, **kwargs):
        """
        Customize the form during initialization:
        - Add placeholders to form fields
        - Add CSS classes to style the form fields
        - Remove default labels
        - Set autofocus on the first field (full name)
        """
        super().__init__(*args, **kwargs)  # Call the parent class's initialization method

        # Define a dictionary of placeholders for each field
        placeholders = {
            'full_name': 'Full Name',  # Placeholder for full name
            'email': 'Email Address',  # Placeholder for email
            'phone_number': 'Phone Number',  # Placeholder for phone number
            'country': 'Country',  # Placeholder for country
            'postcode': 'Postal Code',  # Placeholder for postal code
            'town_or_city': 'Town or City',  # Placeholder for town or city
            'street_address1': 'Street Address 1',  # Placeholder for street address 1
            'street_address2': 'Street Address 2',  # Placeholder for street address 2
            'county': 'County',  # Placeholder for county
        }

        # Set autofocus on the 'full_name' field
        self.fields['full_name'].widget.attrs['autofocus'] = True
        
        # Loop through each form field to customize its attributes
        for field in self.fields:
            # If the field is required, add an asterisk (*) to the placeholder
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            
            # Set the placeholder attribute for the field
            self.fields[field].widget.attrs['placeholder'] = placeholder
            
            # Add a CSS class to style the field
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            
            # Remove the auto-generated label (set label to False)
            self.fields[field].label = False
