from django.db import models


class Food(models.Model):
    """Represents a food item with pricing information and an image."""

    name = models.CharField(max_length=150, verbose_name="Food Name")
    image = models.ImageField(upload_to="foods/", verbose_name="Food Image")
    min_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Minimum Price")
    max_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Maximum Price")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Food"
        verbose_name_plural = "Foods"

    def __str__(self):
        return self.name
