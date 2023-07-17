from django.urls import path
from .views import SnackListView,SnackDetailView,SnackCreateView,SnackUpdateView,SnackDeleteView
urlpatterns = [
    path('', SnackListView.as_view(), name = 'snacks_list'),
    path('<int:pk>/',SnackDetailView.as_view(), name = 'snacks_detail'),
    path('create/',SnackCreateView.as_view(), name = 'snacks_create'),
    path('update/<int:pk>', SnackUpdateView.as_view(), name = 'snacks_update'),
    path('delete/<int:pk>/',SnackDeleteView.as_view(), name = 'snacks_delete'),

]