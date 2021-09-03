"""Members app admin"""
from django.contrib import admin

# Register your models here.
from apps.members.models import Institution


class InstitutionAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'old_name', )
    list_display = ('name', 'slug', 'old_name', 'deleted_at', )
    # [field.name for field in Institution._meta.fields if field.name != "id"]

    def get_queryset(self, request):
        qs = Institution.all_objects.all()
        return qs


admin.site.register(Institution, InstitutionAdmin)
