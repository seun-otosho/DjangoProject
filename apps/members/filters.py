import django_filters
from django import forms
from django.db import models
from django.db.models import QuerySet

from apps.members.models import Institution


class RecordStatusChoices(models.TextChoices):
    ALL = "all"
    LIVE = "open"
    NOT_LIVE = "disabled"


class InstitutionFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    completeness = django_filters.ChoiceFilter(
        choices=RecordStatusChoices.choices,
        widget=forms.widgets.RadioSelect,
        empty_label=None,
        method="get_liveness",
    )

    class Meta:
        model = Institution
        fields = ["name", "old_name", "deleted_at"]

    def get_liveness(
            self, queryset: QuerySet[Institution], field_name: str, value: str
    ) -> QuerySet[Institution]:
        if value == RecordStatusChoices.LIVE:
            return queryset.filter(id__in=[insttxn.id for insttxn in queryset if insttxn.is_active])
        elif value == RecordStatusChoices.NOT_LIVE:
            return queryset.exclude(id__in=[insttxn.id for insttxn in queryset if insttxn.is_active])
        return queryset
