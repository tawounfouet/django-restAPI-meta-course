from django.shortcuts import render
from rest_framework import generics

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
from .models import MenuItem
from .serializers import MenuItemSerializer


# @api_view()
# def menu_items(request):
#     items = MenuItem.objects.select_related('category').all()
#     serialized_items = MenuItemSerializer(items, many=True)
#     return Response(serialized_items.data)
#     #return Response(items.values())

# @api_view()
# def single_item(request, id):
#     item = MenuItem.objects.get(id=id)
#     serialized_item = MenuItemSerializer(item)
#     return Response(serialized_item.data)


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


