from django.urls import path
from . import views

urlpatterns = [
    path('tables/', views.TableList.as_view(), name='table_list'),
]