from store.models import Product
from rest_framework import response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return response.Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=201)
        return response.Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        return response.Response(status=404)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return response.Response(serializer.data)   

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        product.delete()
        return response.Response(status=204)