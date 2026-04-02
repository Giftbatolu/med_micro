from django.urls import path
from .views import MicroListCreateView

urlpatterns = [
    path('micro/', MicroListCreateView.as_view(), name='micro'),
]