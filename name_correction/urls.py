from django.urls import path
from .views import NameCorrectionAPIView

urlpatterns = [
    path('suggest/', NameCorrectionAPIView.as_view(), name='name-correction'),
]
