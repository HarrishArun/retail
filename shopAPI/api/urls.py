from django.urls import path
from . import views
urlpatterns = [
    path('products/all',views.getProducts),
    # path('transactions/<id>',views.getRecommendation)
    path('products/<id>/getRecommendations',views.getRecommendation)
]

