from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ 
    A view to show all products, including sorting and search queries 
    """

    # Fetch all products from the database initially
    products = Product.objects.all()
    
    # Variables to store search, category, sorting, and direction parameters
    query = None
    categories = None
    sort = None
    direction = None

    # Check if there are any GET parameters in the request
    if request.GET:
        # Handle sorting logic
        if 'sort' in request.GET:
            sortkey = request.GET['sort']  # Get the sort key from the request
            sort = sortkey  # Store the original sort key for later use
            # If sorting by product name, add annotation to sort by lowercase version
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))  # Annotate products with lowercase name for sorting
            
            if sortkey == 'category':
                sortkey = 'category__name'

            # Check if the sorting direction (ascending/descending) is specified
            if 'direction' in request.GET:
                direction = request.GET['direction']  # Get the sort direction
                if direction == 'desc':
                    sortkey = f'-{sortkey}'  # If descending, prefix the sort key with '-'
            # Apply sorting to the products queryset
            products = products.order_by(sortkey)
            
        # Handle category filtering logic
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')  # Get selected categories as a list
            # Filter products by the selected categories
            products = products.filter(category__name__in=categories)
            # Retrieve category objects for displaying selected categories
            categories = Category.objects.filter(name__in=categories)

        # Handle search query logic
        if 'q' in request.GET:
            query = request.GET['q']  # Get the search query
            # If no search term is entered, display an error message and redirect
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            # Construct a query to search for the term in product names or descriptions
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            # Filter products based on the search query
            products = products.filter(queries)

    # Combine sorting and direction for use in the template
    current_sorting = f'{sort}_{direction}'

    # Create context dictionary to pass data to the template
    context = {
        'products': products,  # Filtered and sorted products
        'search_term': query,  # The search query used
        'current_categories': categories,  # Selected categories
        'current_sorting': current_sorting,  # Sorting information
    }

    # Render the 'products' template with the context data
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ 
    A view to show individual product details 
    """

    # Retrieve the product using the product_id or return a 404 if not found
    product = get_object_or_404(Product, pk=product_id)

    # Create context dictionary to pass data to the template
    context = {
        'product': product,  # The product object to display
    }

    # Render the 'product_detail' template with the context data
    return render(request, 'products/product_detail.html', context)
