from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    """
    The 'fields' option isn't absolutely necessary here, but it's
    here to allow us to specify the order of the fields in the admin interface,
    which would otherwise be adjusted by Django due to the use of some
    read-only fields.
    This way the order of the fields stays the same as it appears in the model.
    """
    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total',)

    """
    list_display option will restrict the columns that show up in
    the order list to only a few key items.
    """
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    # Set a reverse chronological order: the most recent orders put at the top.
    ordering = ('-date',)
