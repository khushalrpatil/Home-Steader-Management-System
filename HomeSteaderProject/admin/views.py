from django.shortcuts import redirect, render
from products.models import Product, Report
from agency.models import Agency
from django.contrib.admin.views.decorators import user_passes_test
from datetime import datetime, timedelta

from django.contrib.auth import logout


# Create your views here.
@user_passes_test(lambda u: u.is_staff, login_url="admin:login")
def products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def agencies(request):
    agencies = Agency.objects.all()
    return render(request, "adminagency.html", {"agencies": agencies})


# def reports(request):
#     reports = Report.objects.all()
#     return render(request, "reports.html", {"reports": reports})
# def signout(request):
#     logout(request)
#     return redirect("index")
def custom_logout(request):
    logout(request)
    return render(request, 'index.html')
