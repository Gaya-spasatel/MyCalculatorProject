from django.urls import path

from . import views

urlpatterns = [
    path('add', views.SumOperationView.as_view()),
    path('sub', views.DiffOperationView.as_view()),
    path('mul', views.MulOperationView.as_view()),
    path('div', views.DivOperationView.as_view())
]