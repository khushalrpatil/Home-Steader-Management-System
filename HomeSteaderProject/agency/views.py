from django.shortcuts import redirect, render
from .models import Agency, Request


# Create your views here.
def all(request):
    data = Agency.objects.filter(approved=True)
    context = {"data": data}
    return render(request, "showagency.html", context)


def info(request, name):
    data = Agency.objects.get(name=name)
    context = {"data": data}
    return render(request, "agencyinfo.html", context)


def login(request):
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]
        # if Agency.objects.filter(name=name, password=password, approved=True).exists():
        #     agency = Agency.objects.get(name=name, password=password, approved=True)
        #     data = Request.objects.filter(agency=agency.id)
        #     request.session["id"] = agency.id
        #     return render(request, "agency.html", {"data": data})
        # else:
        #     return render(request, "agency-register.html")
        try:
            agency = Agency.objects.get(name=name, password=password)
            if not agency.approved:
                return render(
                    request, "agency-register.html", {"message": "Not Approved Yet"}
                )
            else:
                data = Request.objects.filter(agency=agency.id)
                request.session["id"] = agency.id
                return render(request, "agency.html", {"data": data})
        except Agency.DoesNotExist:
            return render(
                request, "agency-register.html", {"message": "Not Registered"}
            )


def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        contact_person = request.POST["contact_person"]
        phone_number = request.POST["phone_number"]
        email = request.POST["email"]
        password = request.POST["password"]
        image = request.FILES["image"]
        Agency(
            name=name,
            contact_person=contact_person,
            phone_number=phone_number,
            email=email,
            password=password,
            image=image,
        ).save()
        return render(request, "index.html")


def request_training(request):
    if request.method == "POST":
        agency_id = request.POST["agency_id"]
        # print(agency_id)
        agency = Agency.objects.get(pk=agency_id)
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        location = request.POST["location"]

        Request.objects.create(
            agency=agency, name=name, email=email, phone=phone, location=location
        )
    return redirect("all")


def delete(request, id):
    Request.objects.get(id=id).delete()
    id = request.session.get("id", None)
    data = Request.objects.filter(agency=id)
    return render(request, "agency.html", {"data": data})


def logout(request):
    del request.session["id"]
    return render(request, "index.html")
