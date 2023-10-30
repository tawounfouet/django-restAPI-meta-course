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


# Using csrf_exempt decorator
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



# Without using api_view decorator
# def books(request):
#     return HttpResponse('List of the books', status=status.HTTP_200_OK)


# Using api_view decorator 
@api_view(['GET', 'POST'])
def books(request):
    return Response('List of the books', status=status.HTTP_200_OK)

# Using api_view decorator and context parameter
# @api_view()
# def books(request):
#     books = [
#         {'id': 1, 'title': 'Book 1'},
#         {'id': 2, 'title': 'Book 2'},
#     ]
#     return Response({'List of the books': books},  status=status.HTTP_200_OK)



# Using class based views
from rest_framework.views import APIView

class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if (author):
            return Response({"message":"list of the books by " + author}, status=status.HTTP_200_OK)
        
        return Response({"message":"List of the books"}, status=status.HTTP_200_OK)
    
    def post(self, request):
        #title = request.data.get('title')
        #return Response({"message":"new book created"}, status=status.HTTP_201_CREATED)

        # Using payload : a payload is a body of data sent through POST method
        return Response({"title":request.data.get('title')}, status=status.HTTP_201_CREATED)
        #return Response({"title":title}, status=status.HTTP_201_CREATED)


class Book(APIView):
    def get(self, request, pk):
        return Response({"message":"Single book with id " + str(pk)}, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        return Response({"title":request.data.get('title')}, status=status.HTTP_200_OK)
