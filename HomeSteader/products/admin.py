from django.contrib import admin
from .models import Product, Report
from django.http import HttpResponse
from openpyxl import Workbook


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "category", "price", "image")
    list_filter = ["category"]
    list_editable = ["price"]


admin.site.register(Product, ProductAdmin)


def export_reports_to_excel(modeladmin, request, queryset):
    # Create a new Excel workbook and add a worksheet.
    wb = Workbook()
    ws = wb.active

    # Write header row
    headers = ["User", "Product", "Quantity", "Price", "Date", "Status"]
    ws.append(headers)

    # Write data rows
    for report in queryset:
        # Convert timezone-aware datetime to timezone-naive before exporting
        naive_date = report.date.replace(tzinfo=None) if report.date else None
        row_data = [
            report.user,
            report.product,
            report.quantity,
            report.price,
            naive_date,
            report.status,
        ]
        ws.append(row_data)

    # Create response
    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = "attachment; filename=report_data.xlsx"
    wb.save(response)

    return response


export_reports_to_excel.short_description = "Export selected reports to Excel"


@admin.register(Report)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "quantity", "price", "date", "status")
    actions = ["changeStatus", export_reports_to_excel]
    list_filter = ["date", "status"]

    def changeStatus(self, request, queryset):
        queryset.update(status="Delivered")

    changeStatus.short_description = "Change Status"
