from django.urls import path

from apps.members import views

urlpatterns = [
    path('members/', views.display_institutions, name='display_institutions'),
    path('members/<int:id>/delete/', views.delete_institution, name='delete_institution'),
]
