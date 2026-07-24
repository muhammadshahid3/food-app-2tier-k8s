from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import FoodForm
from .models import Food


class FoodListView(ListView):
    """Display the landing page and a list of food records."""

    model = Food
    template_name = "foods/home.html"
    context_object_name = "foods"
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Food.objects.filter(name__icontains=query)
        return Food.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FoodForm()
        return context


class FoodCreateView(CreateView):
    """Handle food creation from the modal form."""

    model = Food
    form_class = FoodForm
    template_name = "foods/home.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Food created successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foods"] = Food.objects.all()
        context["show_modal"] = True
        return context


class FoodUpdateView(UpdateView):
    """Handle updating an existing food item from the modal form."""

    model = Food
    form_class = FoodForm
    template_name = "foods/home.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Food updated successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foods"] = Food.objects.all()
        context["show_modal"] = True
        context["editing_food"] = self.object
        return context


class FoodDeleteView(DeleteView):
    """Delete a food item after confirmation."""

    model = Food
    success_url = reverse_lazy("home")
    http_method_names = ["post"]

    def form_valid(self, form):
        messages.success(self.request, "Food deleted successfully.")
        return super().form_valid(form)
