from django.urls import path

from apps.cheques import views

urlpatterns = [
    path('customers/cheques/fbv/', views.display_cheques, name='display_cheques'),
]
