from django.shortcuts import render
from django.http import HttpResponse

tax_rate = 0.15
# Create your views here.
def index(request):
    return render(request, r"D:\DjangoCourse\Tax\TaxApp\templates\index.html")

def anyNumber(request, price):
    price = float(price)
    total = price + (price * tax_rate)
    return render(request, r"D:\DjangoCourse\Tax\TaxApp\templates\anyNumber.html", {'total': total})

def TaxRate(request):
    return render(request, r'D:\DjangoCourse\Tax\TaxApp\templates\TaxRate.html', {'tax_rate': str(tax_rate)})