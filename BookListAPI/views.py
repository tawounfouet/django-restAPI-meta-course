from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# @csrf_exempt
# def books(request):
#     if request.method == 'GET':
#         books = Book.objects.all().values()
#         return JsonResponse({"books":list(books)})
#     elif request.method == 'POST':
#         title = request.POST.get('title')
#         author = request.POST.get('author')
#         price = request.POST.get('price')
#         book = Book(
#             title = title,
#             author = author,
#             price = price
#         )
#         try:
#             book.save()
#         except IntegrityError:
#             return JsonResponse({'error':'true','message':'required field missing'},status=400)

#         return JsonResponse(model_to_dict(book), status=201)



@api_view(['GET', 'POST'])
def books(request):
    return Response('List of the books', status=status.HTTP_200_OK)


# @api_view()
# def books(request):
#     books = [
#         {'id': 1, 'title': 'Book 1'},
#         {'id': 2, 'title': 'Book 2'},
#     ]
#     return Response({'List of the books': books},  status=status.HTTP_200_OK)