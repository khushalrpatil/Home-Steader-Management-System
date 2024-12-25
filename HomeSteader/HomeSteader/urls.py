"""
URL configuration for HomeSteader project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

admin.site.site_header = "HomeSteader"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("about/", views.about),
    path("services", views.services),
    path("contact/", views.contact),
    path("agencyregister/", views.agencyregister),
    path("register", views.register),
    path("reg/", views.reg),
    path("farmlogin/", views.farmlogin, name="farmlogin"),
    path("signout/", views.signout),
    path("check", views.check),
    path("cart/", views.cart),
    path("product/", include("products.urls")),
    path("agency/", include("agency.urls")),
    path("myadmin/", include("admin.urls")),
    path(
        "delete_selected_products/",
        views.delete_selected_products,
        name="delete_selected_products",
    ),
    path(
        "delete_selected_reports/",
        views.delete_selected_reports,
        name="delete_selected_reports",
    ),
    path("monthly/", views.monthly, name="monthly"),
    path("daily/", views.daily, name="daily"),
    path("reports/", views.reports, name="reports"),
    path("weekly/", views.weekly, name="weekly"),
    path("status/<int:id>/", views.status),
    path("changestatus/<int:id>/", views.changestatus),
    path("users/", views.users),
    path("subadmin/<int:id>", views.subadmin),
    path("deleteuser/<int:id>", views.deleteuser),
    path("climate/", views.climate),
    path("product_list/<str:category>/", views.product_list, name="product_list"),
    path("update_price/<int:product_id>/", views.update_price, name="update_price"),
    path("updateproduct", views.updateproduct, name="updateproduct"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
