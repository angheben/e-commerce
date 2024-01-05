from django.db import models
from django.contrib.auth.models import User
from stdimage.models import StdImageField


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        """
        Rewriting this class to display the plural name correctly and put in alphabetic order
        """
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    """
    This class will server to display the descriptions of an item of our e-commerce
    """
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = StdImageField('Image', upload_to='media', variations={"thumb": {"width": 480, 'height': 480, 'crop': True}})
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
