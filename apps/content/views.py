from django.shortcuts import render, get_object_or_404

from .models import Restaurant, Dish

def restaurant_detail(request, restaurant_slug):
    restaurant = get_object_or_404(Restaurant, slug=restaurant_slug)
    dishes = Dish.objects.filter(restaurant=restaurant)

    context = {
        'restaurant': restaurant,
        'dishes': dishes,
    }

    return render(request, 'restaurant_detail.html', context)

def dish_detail(request, restaurant_slug, dish_slug):
    restaurant = get_object_or_404(Restaurant, slug=restaurant_slug)
    dish = get_object_or_404(Dish, slug=dish_slug)

    context = {
        'restaurant': restaurant,
        'dish': dish,
    }

    return render(request, 'dish_detail.html', context)