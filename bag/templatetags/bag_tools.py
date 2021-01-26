from django import template

# Our custom subtotal template filter


def calc_subtotal(price, quantity):
    return price * quantity
