from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('categories', views.CategoriesView.as_view()),
    path('menu-items/', views.menu_items),
    path('menu-items/<int:id>/', views.single_item),
    path('secret/', views.secret),
    path('api-token-auth/', obtain_auth_token),
    path('me/', views.me),
    path('manager-view/', views.manager_view),
    path('throttle_check/', views.throttle_check),
    path('throttle_check_auth', views.throttle_check_auth),
    #path('menu-items', views.MenuItemsView.as_view()),
     #path('menu-items/<int:id>/', views.SingleMenuItemView.as_view()),
    # path('menu-items',views.MenuItemsViewSet.as_view({'get':'list'})),
    # path('menu-items/<int:pk>',views.MenuItemsViewSet.as_view({'get':'retrieve'})),

]