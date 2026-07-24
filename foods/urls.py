from django.urls import path
from .views import FoodListView, FoodCreateView, FoodUpdateView, FoodDeleteView

urlpatterns = [
    path("", FoodListView.as_view(), name="home"),
    path("add-food/", FoodCreateView.as_view(), name="add_food"),
    path("update-food/<int:pk>/", FoodUpdateView.as_view(), name="update_food"),
    path("delete-food/<int:pk>/", FoodDeleteView.as_view(), name="delete_food"),
]
