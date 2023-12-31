from django.shortcuts import render
from rest_framework import generics

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer


# @api_view()
# def menu_items(request):
#     items = MenuItem.objects.select_related('category').all()
#     serialized_items = MenuItemSerializer(items, many=True)
#     return Response(serialized_items.data)
#     #return Response(items.values())


# Managing Get and Post Requests on the same endpoint
@api_view(["GET", "POST"])
def menu_items(request):
    # Get Request
    if request.method == "GET":
        items = MenuItem.objects.select_related("category").all()
        # Seaching, Filtering and Ordering
        category_name = request.query_params.get("category")
        to_price = request.query_params.get("to_price")
        search = request.query_params.get("search")
        ordering = request.query_params.get("ordering")
        # Pagination
        perpage = request.query_params.get("perpage", default=2)
        page = request.query_params.get("page", default=1)
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price)
        if search:
            items = items.filter(title__icontains=search)
        if ordering:
            # items = items.order_by(ordering)
            # ordering with multiple fields
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)
        # Pagination
        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []

        serialized_items = MenuItemSerializer(items, many=True)
        return Response(serialized_items.data)
    # Post Request
    elif request.method == "POST":
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status=status.HTTP_201_CREATED)


@api_view()
def single_item(request, id):
    item = MenuItem.objects.get(id=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ["price", "inventory"]
    filterset_fields = ["price", "inventory"]
    search_fields = ["title"]


from rest_framework import viewsets


class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ["price", "inventory"]
    search_fields = ["title", "category__title"]


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, throttle_classes


@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message": "This is a secret message"}, status=status.HTTP_200_OK)


@api_view()
@permission_classes([IsAuthenticated])
def me(request):
    return Response(request.user.email, status=status.HTTP_200_OK)


@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name="Manager").exists():
        return Response(
            {"message": "Welcome to the manager view"}, status=status.HTTP_200_OK
        )
    else:
        return Response(
            {"message": "You are not allowed to access this view"},
            status=status.HTTP_403_FORBIDDEN,
        )


from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .throttles import TenCallsPerMinute


@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message": "Sucessfull"}, status=status.HTTP_200_OK)


@api_view()
@permission_classes([IsAuthenticated])
# @throttle_classes([UserRateThrottle])
@throttle_classes([TenCallsPerMinute])
def throttle_check_auth(request):
    return Response(
        {"message": "Message for the logged in users only"}, status=status.HTTP_200_OK
    )


from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404

@api_view(["POST"])
@permission_classes([IsAdminUser])
def managers(request):
    username = request.data["username"]
    if username:
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="Manager")
        if request.method == "POST":
            managers.user_set.add(user)
        elif request.method == "DELETE":
            managers.user_set.remove(user)
        return Response({"message": "Ok"}, status=status.HTTP_200_OK)
    
    return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)


from .models import Rating
from .serializers import RatingSerializer

class RatingsView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if(self.request.method=='GET'):
            return []

        return [IsAuthenticated()]
