from django.urls import path
from .views import MicroListCreateView

urlpatterns = [
    path('', MicroListCreateView.as_view(), name='micro'),
]