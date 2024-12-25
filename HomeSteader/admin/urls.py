from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("products/", views.products, name="products"),
    path("agencies/", views.agencies, name="agencies"),
    # path("logout/", LogoutView.as_view(next_page=""), name="logout"),
    # path("reports/", views.reports, name="reports"),
    path("logout/", views.custom_logout, name="logout"),
]
