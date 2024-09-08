from django.shortcuts import render

# Create your views here.
# This file contains the views for the 'home' app

""" 
A view to return the index.html template 
This function handles the request for the homepage.
"""

def index(request):
    # Renders and returns the 'index.html' template located in the 'home' directory
    return render(request, 'home/index.html')
