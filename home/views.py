from django.shortcuts import render

# Create your views here.

""" A view to return index.html  """

def index(request):
    return render(request, 'home/index.html')