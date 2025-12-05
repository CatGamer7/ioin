from django.urls import path
from .views import ClassifyText, MessageStatsView


urlpatterns = [
    path('classify/', ClassifyText.as_view(), name='classify'),
    path('stats/<str:chat_id>/', MessageStatsView.as_view(), name='message-stats'),
]
