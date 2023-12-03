from django.shortcuts import render

from apps.content.models import Restaurant

def home(request):
    restaurants = Restaurant.objects.all()

    context = {
        'restaurants': restaurants
    }

    return render(request, 'home.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')