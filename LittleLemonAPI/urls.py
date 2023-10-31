from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.CategoriesView.as_view()),
    path('menu-items/', views.menu_items),
    path('menu-items/<int:id>/', views.single_item),
    #path('menu-items', views.MenuItemsView.as_view()),
     #path('menu-items/<int:id>/', views.SingleMenuItemView.as_view()),
    # path('menu-items',views.MenuItemsViewSet.as_view({'get':'list'})),
    # path('menu-items/<int:pk>',views.MenuItemsViewSet.as_view({'get':'retrieve'})),

]