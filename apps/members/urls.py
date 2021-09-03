from django.urls import path

from apps.members import views
from apps.members.views import InstitutionListView, InstitutionFilterView, InstitutionCreateView

urlpatterns = [
    path("members/", InstitutionListView.as_view(), name="institutions-list"),
    path("filter/", InstitutionFilterView.as_view(), name="institutions-filter"),
    path("create/", InstitutionCreateView.as_view(), name="institution-create"),

    path('members/fbv/', views.display_institutions, name='display_institutions'),
    path('members/<int:id>/delete/', views.delete_institution, name='delete_institution'),
]
