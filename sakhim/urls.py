"""
URL configuration for sakhim project.
The `urlpatterns` list routes URLs to views. For more information, see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
from django.contrib import admin  # Ensure 'django' is installed
from django.urls import include, path
from django.conf.urls.static import static
from sakhim import settings, views

urlpatterns = [
                  path('admin_honeypot/', include('admin_honeypot.urls', namespace='admin_honeypot')),
                  path('securelogin/', admin.site.urls),
                  path('', views.home, name='home'),  # Ensure 'views.home' is implemented correctly
                  path('store/', include('store.urls')),
                  path('cart/', include('carts.urls')),
                  path('accounts/', include('accounts.urls')),
                  # ORDERS
                  path('orders/', include('orders.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
