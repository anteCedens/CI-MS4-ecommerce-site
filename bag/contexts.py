from decimal import Decimal
from django.conf import settings


"""
This function will return a dictionary (instead of a template, for instance)
called 'context'.
This is what's known as a 'context processor'.
It's purpose is to make this dictionary available to all templates
across the entire app.
In order for this to work, we need to add it to the list of
context processors in settings.py
"""


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    
    context = {
        
    }

    return context