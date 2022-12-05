from django.urls import path
from .views import SnackListView,SnackDetailView,SnackCreateView
urlpatterns = [
    path('',SnackListView.as_view(),name='snack_list'),
    path('<int:pk>/',SnackDetailView.as_view(),name='detail_list'),
    path('create',SnackCreateView.as_view(),name='create_list')
]