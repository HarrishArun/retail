from django.urls import path
from . import views
urlpatterns = [
    path('users',views.getAllUsers),
    path('users/<id>',views.getUser),
    path('addUser',views.addUser),
    path('updateTransaction/<id>',views.addTransation)
]
