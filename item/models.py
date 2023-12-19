from django.db import models


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

