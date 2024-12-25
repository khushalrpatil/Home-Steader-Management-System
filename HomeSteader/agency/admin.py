from django.contrib import admin
from .models import Agency


# Register your models here.
@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "contact_person",
        "phone_number",
        "email",
        "approved",
        "image",
    )
    list_filter = ["approved"]
    actions = ["approve_agency"]

    def approve_agency(self, request, queryset):
        queryset.update(approved=True)

    approve_agency.short_description = "Approve Selected Agencies"
