"""
'Post', in this case, means after: so this implies these signals
are sent by Django to the entire application after a model instance
is saved and after it's deleted respectively.
"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem


def update_on_save(sender, instance, created, **kwargs):
    # Update order total on lineitem update/create
    instance.order.update_total()
