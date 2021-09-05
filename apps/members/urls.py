from django.urls import path

from apps.members import views
from apps.members.views import InstitutionListView, InstitutionFilterView, InstitutionCreateView, InstitutionDetailView

urlpatterns = [
    path("members/",                InstitutionListView.as_view(),      name="institutions-list"),
    path("filter/instructions/",    InstitutionFilterView.as_view(),    name="institutions-filter"),
    path("create/institution/",     InstitutionCreateView.as_view(),    name="institution-create"),
    path("<slug:slug>/",            InstitutionDetailView.as_view(),    name="institution-detail"),

    path('members/fbv/', views.display_institutions, name='display_institutions'),
    path('members/<int:id>/delete/', views.delete_institution, name='delete_institution'),
]
