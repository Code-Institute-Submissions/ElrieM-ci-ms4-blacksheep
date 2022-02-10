# Imports 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect, reverse

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def product_overview(request):
    """
    A view to show categories and products.
    """
    return render(request, 'products/products.html')


def product_details(request):
    """
    A view to show details of product, select options and add to cart
    """
    return render(request, 'products/product_details.html')


def add_product(request):
    """
    A view for adding new product types and templates. Only administrative users can make changes.
    """
    return render(request, 'products/add_product.html')


def edit_product(request):
    """
    A view for editing existing product types and templates. Only administrative users can make changes.
    """
    return render(request, 'products/edit_product.html')


def delete_product(request):
    """
    A view to delete a product and template.
    """
    return redirect(reverse('products'))
