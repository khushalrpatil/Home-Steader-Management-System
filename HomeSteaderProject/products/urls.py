from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add/", views.add),
    path("addProduct", views.addProduct),
    path("<str:name>/", views.info),
    path("search", views.search),
    path("search", views.search),
    path("buyProduct", views.buyProduct),
    # path("handlerequest", views.handlerequest, name="handlerequest"),
    path("buy/<str:name>/", views.buy),
]
