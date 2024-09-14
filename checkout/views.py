# Import necessary functions from Django
from django.shortcuts import render, redirect, reverse  # Functions for rendering templates and handling redirects
from django.contrib import messages  # For displaying user messages (like error or success notifications)

# Import the OrderForm class from the forms module
from .forms import OrderForm


# Define the checkout view
def checkout(request):
    """
    Handles the checkout process. This function checks if there is a 'bag' (cart) in the session,
    and if not, redirects the user back to the products page with an error message.
    If the bag is present, it initializes an empty order form and renders the checkout page.
    """

    # Retrieve the shopping bag from the session, or initialize it as an empty dictionary if not found
    bag = request.session.get('bag', {})

    # If the bag is empty, display an error message and redirect to the products page
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")  # Show an error message
        return redirect(reverse('products'))  # Redirect to the 'products' page

    # If the bag is not empty, create a new instance of the OrderForm
    order_form = OrderForm()

    # Specify the template to render (checkout page)
    template = 'checkout/checkout.html'

    # Pass the order form into the context to render it in the template
    context = {
        'order_form': order_form,  # Order form object to be displayed in the template
    }

    # Render the checkout template with the provided context
    return render(request, template, context)
