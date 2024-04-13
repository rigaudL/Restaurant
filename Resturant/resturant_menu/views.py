from django.shortcuts import render, redirect
from django.views import generic
from .models import Item, meal_type

class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = meal_type
        return context

def about(request):
    return redirect('home')

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
