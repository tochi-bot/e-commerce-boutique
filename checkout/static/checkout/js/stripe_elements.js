/*
    The core logic and payment flow for this script comes from Stripe's official documentation:
    https://stripe.com/docs/payments/accept-a-payment

    The CSS for styling Stripe's elements comes from here:
    https://stripe.com/docs/stripe-js
*/

// Retrieve the Stripe public key and client secret from the template
// The keys are embedded in the HTML and retrieved using jQuery, with `.slice(1, -1)` to remove quotes
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);

// Initialize the Stripe object with the public key
var stripe = Stripe(stripe_public_key);

// Create an instance of Stripe's elements, which will be used to mount the card input field
var elements = stripe.elements();

// Define custom styles for the Stripe card element
var style = {
    base: {
        color: '#000',  // Text color for the card element
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',  // Font family for card input
        fontSmoothing: 'antialiased',  // Smooth text rendering for better readability
        fontSize: '16px',  // Font size for the input text
        '::placeholder': {
            color: '#aab7c4'  // Placeholder text color
        }
    },
    invalid: {
        color: '#dc3545',  // Color for invalid input or errors (red)
        iconColor: '#dc3545'  // Icon color for invalid states
    }
};

// Create a card element with the defined style
var card = elements.create('card', {style: style});

// Mount the card element into the `#card-element` div in the HTML
card.mount('#card-element');
