from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is a site to calculate tax")

def calculate_tax(request, number):
    tax_rate = 0.15
    total_price = number + (number * tax_rate)
    return HttpResponse(f"The total price after 15% tax is: {total_price}")

def tax_rate(request):
    tax_rate = 0.15
    return render(request, 'tax_rate.html', {'tax_rate': tax_rate})

