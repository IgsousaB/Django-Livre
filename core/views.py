from django.shortcuts import render

from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()

    context = {
        'curso': 'Programação web com Django Framework',
        'outro': ''
    }
    return render(request, 'index.html', context)

def contact(request):
    # context = {
    #
    # }
    return render(request, 'contact.html')
