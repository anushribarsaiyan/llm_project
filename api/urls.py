from django.urls import path
from .views import ProcessTextAPIView, HistoryAPIView

urlpatterns = [
    path('process/', ProcessTextAPIView.as_view(), name='process_text'),
    path('history/', HistoryAPIView.as_view(), name='history')
]
