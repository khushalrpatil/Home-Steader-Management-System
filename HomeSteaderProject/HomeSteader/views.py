from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from products.models import Product, Report
from agency.models import Agency
from datetime import datetime, timedelta
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import re

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def services(request):
    if request.method == "POST":
        name = request.POST["name"]
        data = Product.objects.filter(name__icontains=name)
        context = {"data": data}
        return render(request, "services.html", context)

    data = Product.objects.all()
    context = {"data": data}
    return render(request, "services.html", context)


def contact(request):
    return render(request, "contact.html")


def farmlogin(request):
    return render(request, "farmlogin.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]
        # phone_number = request.POST["phone_number"]
        User.objects.create_user(username=first_name, first_name=first_name, last_name=last_name, email=email,
                                 password=password)
    return redirect("farmlogin")


# def register(request):
#     if request.method == "POST":
#         first_name = request.POST["fname"]
#         last_name = request.POST["lname"]
#         email = request.POST["email"]
#         password = request.POST["password"]
#
#         # Validation
#         if not first_name:
#             messages.error(request, 'Please enter your first name.', extra_tags='fname')
#         elif not re.match("^[a-zA-Z]+$", first_name):
#             messages.error(request, 'First name should contain only letters.', extra_tags='fname')
#
#         if not last_name:
#             messages.error(request, 'Please enter your last name.', extra_tags='lname')
#         elif not re.match("^[a-zA-Z]+$", last_name):
#             messages.error(request, 'Last name should contain only letters.', extra_tags='lname')
#
#         if not email:
#             messages.error(request, 'Please enter your email address.', extra_tags='email')
#         if not password:
#             messages.error(request, 'Please enter your password.', extra_tags='password')
#
#         # If any validation failed, return to the form page
#         if any(messages.get_messages(request)):
#             return render(request, 'reg.html')
#
#         # If all validations pass, create the user
#         User.objects.create_user(username=first_name, first_name=first_name, last_name=last_name, email=email,
#                                  password=password)
#         return redirect("farmlogin")
#
#     # Render the same page for GET requests
#     return render(request, 'reg.html')


def reg(request):
    return render(request, "reg.html")


def check(request):
    if request.method == "POST":
        uname = request.POST["username"]
        password = request.POST["password"]
        data = authenticate(username=uname, password=password)
        if data:
            login(request, data)
            return redirect("/product/dashboard")
        else:
            return redirect("farmlogin")


def cart(request):
    reports = Report.objects.filter(userid=request.user.id)
    return render(request, "cart.html", {"reports": reports})


def signout(request):
    logout(request)
    return redirect("index")


def agencyregister(request):
    return render(request, "agency-register.html")


def delete_selected_products(request):
    if request.method == "POST":
        selected_product_ids = request.POST.getlist("selected_products")
        Product.objects.filter(id__in=selected_product_ids).delete()
    return redirect("/myadmin/products")


def monthly(request):
    current_year = datetime.now().year
    current_month = datetime.now().month

    reports = Report.objects.filter(date__year=current_year, date__month=current_month)

    return render(request, "reports.html", {"reports": reports})


def reports(request):
    reports = Report.objects.all()
    return render(request, "reports.html", {"reports": reports})


def delete_selected_reports(request):
    if request.method == "POST":
        selected_report_ids = request.POST.getlist("selected_reports")
        Report.objects.filter(id__in=selected_report_ids).delete()
    return redirect("/reports")


def daily(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    current_day = datetime.now().day

    reports = Report.objects.filter(
        date__year=current_year, date__month=current_month, date__day=current_day
    )

    return render(request, "reports.html", {"reports": reports})


def weekly(request):
    current_date = datetime.now()
    start_of_week = current_date - timedelta(days=current_date.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    reports = Report.objects.filter(date__range=[start_of_week, end_of_week])

    return render(request, "reports.html", {"reports": reports})


def status(request, id):
    agency = Agency.objects.get(id=id)
    agency.approved = not agency.approved
    agency.save()
    return redirect("/myadmin/agencies")


def changestatus(request, id):
    report = Report.objects.get(id=id)
    if report.status == "Pending":
        report.status = "Delivered"
    else:
        report.status = "Pending"
    report.save()
    return redirect("/reports")


def users(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})


def deleteuser(request, id):
    User.objects.get(id=id).delete()
    return redirect("/users")


def subadmin(request, id):
    user = User.objects.get(id=id)
    user.is_staff = not user.is_staff
    user.save()
    return redirect("/users")


def climate(request):
    return render(request, "climate.html")


def product_list(request, category=None):
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    return render(request, "dashboard.html", {"data": products})


def update_price(request, product_id):
    if request.method == "POST":
        name = request.POST["name"]
        category = request.POST["category"]
        price = request.POST["price"]
        image = request.FILES["image"]
        description = request.POST["description"]
        Product(
            name=name,
            description=description,
            category=category,
            price=price,
            image=image,
        ).save()
    return redirect("/product/dashboard")


def updateproduct(request):
    id = request.POST["id"]
    product = Product.objects.get(id=id)
    product.name = request.POST["name"]
    product.description = request.POST["description"]
    product.price = request.POST["price"]
    product.save()
    return redirect("/myadmin/products")
