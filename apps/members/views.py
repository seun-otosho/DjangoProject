"""Members app views"""
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods

from apps.members.models import Institution


def display_institutions(request):
    institutions = Institution.objects.all()
    return render(request, 'display_institutions.html', {'institutions': institutions})


@require_http_methods(['DELETE'])
def delete_institution(request, id):
    Institution.objects.filter(id=id).delete()
    institutions = Institution.objects.all()
    return render(request, 'institutions_list.html', {'institutions': institutions})
