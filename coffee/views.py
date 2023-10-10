from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Coffee
from .serializers import CoffeeSerializer

@api_view(['GET'])
def coffee_list(request):
    coffees = Coffee.objects.all()
    serializer = CoffeeSerializer(coffees, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_coffee(request):
    serializer = CoffeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def coffee_detail(request, pk):
    try:
        coffee = Coffee.objects.get(pk=pk)
        serializer = CoffeeSerializer(coffee)
        return Response(serializer.data)
    except Coffee.DoesNotExist:
        return Response(status=404)

@api_view(['PUT'])
def update_coffee(request, pk):
    try:
        coffee = Coffee.objects.get(pk=pk)
        serializer = CoffeeSerializer(coffee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except Coffee.DoesNotExist:
        return Response(status=404)

@api_view(['DELETE'])
def delete_coffee(request, pk):
    try:
        coffee = Coffee.objects.get(pk=pk)
        coffee.delete()
        return Response(status=204)
    except Coffee.DoesNotExist:
        return Response(status=404)
