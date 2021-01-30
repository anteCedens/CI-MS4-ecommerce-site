from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    # This is just like a foreign key, except that it specifies
    # that each user can only have one profile,
    # and each profile can only be attached to one user.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
