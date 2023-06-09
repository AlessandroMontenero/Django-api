from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import Dish
from core.serializers import DishSerializer


@api_view(['GET', 'POST'])
def dishes_list(request, format=None):
    """
    List all dishes, or create a new dish.
    """
    if request.method == 'GET':
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def dish_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        dish = Dish.objects.get(pk=pk)
    except Dish.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DishSerializer(dish)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DishSerializer(dish, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
