import base64
from decimal import Decimal

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .forms import FoodForm
from .models import Food


def image_file(name="food.gif"):
    """Return a tiny valid GIF suitable for ImageField tests."""
    content = base64.b64decode("R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==")
    return SimpleUploadedFile(name, content, content_type="image/gif")


class FoodFormTests(TestCase):
    def test_rejects_a_minimum_price_above_maximum_price(self):
        form = FoodForm(data={"name": "Rice", "min_price": "12", "max_price": "10"}, files={"image": image_file()})

        self.assertFalse(form.is_valid())
        self.assertIn("Minimum price cannot be greater", form.non_field_errors()[0])


class FoodViewTests(TestCase):
    def create_food(self, name="Rice"):
        return Food.objects.create(name=name, image=image_file(), min_price=Decimal("10.00"), max_price=Decimal("15.00"))

    def test_home_can_search_the_catalog(self):
        self.create_food("Rice")
        self.create_food("Pasta")

        response = self.client.get(reverse("home"), {"q": "ric"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual([food.name for food in response.context["foods"]], ["Rice"])

    def test_create_and_delete_work_and_deletion_requires_post(self):
        self.assertEqual(self.client.get(reverse("add_food")).status_code, 200)
        response = self.client.post(reverse("add_food"), {"name": "Soup", "image": image_file(), "min_price": "4.50", "max_price": "6.00"})
        self.assertRedirects(response, reverse("home"))
        food = Food.objects.get(name="Soup")

        self.assertEqual(self.client.get(reverse("delete_food", args=[food.pk])).status_code, 405)
        response = self.client.post(reverse("delete_food", args=[food.pk]))

        self.assertRedirects(response, reverse("home"))
        self.assertFalse(Food.objects.filter(pk=food.pk).exists())

# Create your tests here.
