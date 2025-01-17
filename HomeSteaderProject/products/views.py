from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Product, Report
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from paytm import Checksum
MERCHANT_KEY = 'kbzk1DSbJiV_03p5'

def dashboard(request):
    # data = Product.objects.values_list("name", "price", "image")
    # category=request.args.get("category", default=None)
    data = Product.objects.all()
    context = {"data": data}
    return render(request, "dashboard.html", context)


def info(request, name):
    data = Product.objects.get(name=name)
    context = {"data": data}
    return render(request, "info.html", context)


def search(request):
    if request.method == "POST":
        name = request.POST["name"]
        data = Product.objects.filter(name__icontains=name)
        context = {"data": data}
        return render(request, "searched.html", context)


def add(request):
    return render(request, "add.html")


def addProduct(request):
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


def buy(request, name):
    data = Product.objects.get(name=name)
    context = {"data": data}
    return render(request, "buy.html", context)


# @login_required
# def buyProduct(request):
#     if request.method == "POST":
#         userid = User.objects.get(pk=request.user.id)
#         user = request.user.username
#         product = request.POST["product"]
#         quantity = request.POST["quantity"]
#         price = request.POST["total"]
#         date = datetime.now()

#         Report.objects.create(
#             userid=userid,
#             user=user,
#             product=product,
#             quantity=quantity,
#             price=price,
#             date=date,
#         )

#         param_dict = {
#             'MID': 'WorldP64425807474247',  
#             'ORDER_ID': str(userid.id),     # Assuming userid is a User object
#             'TXN_AMOUNT': str(price),       # Total amount to be charged
#             'CUST_ID': str(userid.id),      # Customer ID
#             'INDUSTRY_TYPE_ID': 'Retail',   # Industry type
#             'WEBSITE': 'WEBSTAGING',        # Your staging website
#             'CHANNEL_ID': 'WEB',            # Channel ID
#             'CALLBACK_URL': 'http://127.0.0.1:8000/product/handlerequest',  # Callback URL
#         }

#         param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)

#         return render(request, 'paytm.html', {'param_dict': param_dict})
    
#     return redirect("dashboard")


# @csrf_exempt
# def handlerequest(request):
    # form = request.POST
    # response_dict = {}

    # checksum = None  

    # for i in form.keys():
    #     response_dict[i] = form[i]
    #     if i == 'CHECKSUMHASH':
    #         checksum = form[i]

    # if checksum:
    #     verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    #     if verify:
    #         if response_dict['RESPCODE'] == '01':
    #             print('Order successful')
    #         else:
    #             print('Order was not successful because: ' + response_dict['RESPMSG'])
    # else:
    #     print('CHECKSUMHASH not found in form data')

    # return render(request, 'paymentstatus.html', {'response': response_dict})
    # return HttpResponse("Done")

@login_required
def buyProduct(request):
    if request.method == "POST":
        userid = User.objects.get(pk=request.user.id)
        user = request.user.username
        product = request.POST["product"]
        quantity = request.POST["quantity"]
        price = request.POST["total"]
        phone = request.POST["phone"]
        city = request.POST["city"]
        state = request.POST["state"]
        zip = request.POST["zip"]
        street = request.POST["street"]
        # total = price * quantity
        date = datetime.now()
        Report.objects.create(
            userid=userid,
            user=user,
            product=product,
            quantity=quantity,
            price=price,
            date=date,
            phone=phone,
            city=city,
            state=state,
            zip=zip,
            street=street,
        )
        return redirect("dashboard")