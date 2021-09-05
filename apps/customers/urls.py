from django.urls import path

from apps.customers import views

urlpatterns = [
    # path("members/",                InstitutionListView.as_view(),      name="institutions-list"),
    # path("filter/instructions/",    InstitutionFilterView.as_view(),    name="institutions-filter"),
    # path("create/institution/",     InstitutionCreateView.as_view(),    name="institution-create"),
    # path("<slug:slug>/",            InstitutionDetailView.as_view(),    name="institution-detail"),

    path('customers/fbv/', views.display_customers, name='display_customers'),
    # path('members/<int:id>/delete/', views.delete_institution, name='delete_institution'),
]
