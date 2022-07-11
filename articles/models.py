from django.db import models


class Category(models.Model):
    """The model for the category."""
    category_name = models.CharField(max_length=128)
    is_active = models.BooleanField()

    def __str__(self):
        """Forms a printable representation of the object.
        Returns the name of the category.
        """
        return str(self.category_name)

    class Meta:
        """Defines the model involved and the fields used in the form.
        """
        ordering = ('id',)
