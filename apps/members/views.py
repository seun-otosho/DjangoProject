"""Members app views"""
import json
from typing import Dict, Any

from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, CreateView, DetailView
from django_filters.views import FilterView

from apps.members.filters import InstitutionFilter
from apps.members.forms import InstitutionCreateForm
from apps.members.models import Institution


class InstitutionListView(ListView):
    model = Institution

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        return super().get_context_data(
            form=InstitutionCreateForm(), filterset=InstitutionFilter, **kwargs
        )


class InstitutionFilterView(FilterView):
    filterset_class = InstitutionFilter


class InstitutionCreateView(CreateView):
    model = Institution
    form_class = InstitutionCreateForm
    template_name = "members/institution_create_form.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        institution = form.save()
        response = HttpResponse()
        response["HX-Trigger"] = json.dumps(
            {"redirect": {"url": institution.get_absolute_url()}}
        )
        return response


class InstitutionDetailView(DetailView):
    model = Institution


def display_institutions(request):
    institutions = Institution.objects.all()
    return render(request, 'display_institutions.html', {'institutions': institutions})


@require_http_methods(['DELETE'])
def delete_institution(request, id):
    Institution.objects.filter(id=id).delete()
    institutions = Institution.objects.all()
    return render(request, 'members_list.html', {'institutions': institutions})
