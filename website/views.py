from django.shortcuts import render, redirect
from .models import Products
from django.core.paginator import Paginator


# products = Products.objects.all()


def index(request):
    products = Products.objects.order_by("?")
    return render(request, "index.html")


def electronics(request):
    products = Products.objects.order_by("?")
    return render(request, "electronics.html", {"products": products})


def other(request):
    products = Products.objects.order_by("?")
    return render(request, "others.html", {"products": products})


def home(request):
    products = Products.objects.order_by("?")
    return render(request, "home.html", {"products": products})


def others(request):
    products = Products.objects.order_by("?")
    return render(request, "others.html", {"products": products})


def fashion(request):
    products = Products.objects.order_by("?")
    return render(request, "fashion.html", {"products": products})


def allproducts(request):
    products = Products.objects.order_by("?")
    return render(request, "allproducts.html", {"products": products})


def mobile(request):
    products = Products.objects.order_by("?")
    return render(request, "electronics/mobile.html", {"products": products})


def computer(request):
    products = Products.objects.order_by("?")
    return render(request, "electronics/computer.html", {"products": products})


def contact(request):
    products = Products.objects.order_by("?")
    return render(request, "contact.html", {"products": products})


def dummystand(request):
    products = Products.objects.order_by("?")
    return render(request, "fashion/garments/dummystand.html", {"products": products})


def girlsgarment(request):
    products = Products.objects.order_by("?")
    return render(request, "fashion/garments/girlsgarment.html", {"products": products})


def femalegarment(request):
    products = Products.objects.order_by("?")   
    return render(
        request, "fashion/garments/femalegarment.html", {"products": products}
    )


def boysgarment(request):
    products = Products.objects.order_by("?")
    return render(request, "fashion/garments/boysgarment.html", {"products": products})


def malegarment(request):
    products = Products.objects.order_by("?")
    return render(request, "fashion/garments/malegarment.html", {"products": products})


def femalefootwear(request):
    products = Products.objects.order_by("?")
    return render(
        request, "fashion/footwear/femalefootwear.html", {"products": products}
    )


def boysfootwear(request):
    products = Products.objects.order_by("?")
    return render(request, "fashion/footwear/boysfootwear.html", {"products": products})


def girlsfootwear(request):
    products = Products.objects.order_by("?")
    return render(
        request, "fashion/footwear/girlsfootwear.html", {"products": products}
    )


def kidsfootwear(request):
    products = Products.objects.order_by("?")
    return render(request, "fashion/footwear/kidsfootwear.html", {"products": products})


def malefootwear(request):
    products = Products.objects.order_by("?")
    return render(request, "fashion/footwear/malefootwear.html", {"products": products})


def perfume(request):
    products = Products.objects.order_by("?")
    return render(request, "fashion/personal_care/perfume.html", {"products": products})


def cosmetics(request):
    products = Products.objects.order_by("?")  
    return render(
        request, "fashion/personal_care/cosmetics.html", {"products": products}
    )


def google(request):
    products = Products.objects.order_by("?")
    return render(request, "fashion/accesories/google.html", {"products": products})


def wallet(request):
    products = Products.objects.order_by("?")
    return render(request, "fashion/accesories/wallet.html", {"products": products})


def jwellery(request):
    products = Products.objects.order_by("?")
    return render(request, "fashion/accesories/jwellery.html", {"products": products})


def watches(request):
    products = Products.objects.order_by("?")
    return render(request, "fashion/accesories/watches.html", {"products": products})


def belt(request):
    products = Products.objects.order_by("?")
    return render(request, "fashion/accesories/belt.html", {"products": products})


def seagenable(request):
    products = Products.objects.order_by("?")
    return render(request, "fashion/accesories/seagenable.html", {"products": products})


def gifts(request):
    products = Products.objects.order_by("?")
    return render(request, "others/gifts.html", {"products": products})


def play(request):
    products = Products.objects.order_by("?")
    return render(request, "others/play.html", {"products": products})


def sport(request):
    products = Products.objects.order_by("?")
    return render(request, "others/sport.html", {"products": products})


def crockery(request):
    products = Products.objects.order_by("?")
    return render(request, "home/crockery.html", {"products": products})


def handloom(request):

    products = Products.objects.order_by("?")
    return render(request, "home/handloom.html", {"products": products})


def plastic(request):   
    products = Products.objects.order_by("?")
    return render(request, "home/plastic.html", {"products": products})


def cleaning(request):
    products = Products.objects.order_by("?")
    return render(request, "home/cleaning.html", {"products": products})


def tools(request):
    products = Products.objects.order_by("?")
    return render(request, "home/tools.html", {"products": products})


def kitchenware(request):
    products = Products.objects.order_by("?")
    return render(request, "home/kitchenware.html", {"products": products})
