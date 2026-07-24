from django.contrib import admin
from .models import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    """Admin configuration for the Food model."""

    list_display = ("name", "min_price", "max_price", "created_at")
    search_fields = ("name",)
    list_filter = ("created_at",)
