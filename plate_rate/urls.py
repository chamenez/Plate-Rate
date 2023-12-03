
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.core.views import home, contact, about
from apps.content.views import restaurant_detail, dish_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('<slug:restaurant_slug>/', restaurant_detail, name='restaurant_detail'),
    path('<slug:restaurant_slug>/<slug:dish_slug>/', dish_detail, name='dish_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
