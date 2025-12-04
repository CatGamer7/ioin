from django.urls import path
from .views import ClassifyText


urlpatterns = [
    path('classify/', ClassifyText.as_view(), name='classify'),
]
