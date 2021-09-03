from django import forms
from django.utils.text import slugify

from apps.members.models import Institution


class InstitutionCreateForm(forms.ModelForm):
    slug = forms.CharField(required=False, widget=forms.widgets.HiddenInput())

    class Meta:
        model = Institution
        fields = ("name", "slug")

    def clean_name(self) -> str:
        name: str = self.cleaned_data["name"]
        slug = slugify(name)
        if Institution.objects.filter(slug=slug).exists():
            raise forms.ValidationError(f"An Institution with the name {name} exists")
        return name

    def save(self, commit: bool = True) -> Institution:
        institution: Institution = super().save(commit)
        institution.slug = slugify(institution.name)
        institution.save()
        return institution
