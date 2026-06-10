from django.urls import path
from . import views

urlpatterns = [
    path('makeorder/', views.MakeOrder.as_view()),
    path('details/<pk>/',views.Delivery.as_view()),
    path('reviews/',views.ReviwsList.as_view()),
    path('reviews/<pk>/',views.ReviewUpdate.as_view()),
    # path('makeorder/',views.makeOrder),
    # path('delivery/',views.delivery),
    # path('details/<pk>/',views.details)
    
]