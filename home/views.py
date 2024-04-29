from django.shortcuts import render
from django.views import View
from product.models import Product


class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'home/home.html', {'products': products})
