from django.urls import path

from apps.facilities import views

urlpatterns = [
    path('customers/facilities/fbv/', views.display_facilities, name='display_facilities'),
]
