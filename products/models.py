from django.db import models

# Create your models here.


class Category(models.Model):

    """
    Use the 'Meta' class to change the Django
    inherent (mis)spelling of 'Categorys'
    """
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ManyToManyField(
        'Category', blank=True, help_text='Select a category for this book')
    """
    Each product will require a name, author, and price,
    but everything else is set as optional
    """
    sku = models.CharField('SKU', max_length=254, null=True, blank=True)
    name = models.TextField(max_length=254)
    author = models.CharField(max_length=254)
    publisher_name = models.CharField(max_length=254, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    # image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
