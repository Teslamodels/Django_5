from django.urls import path
from .views import Elon, Musk

urlpatterns = [
    path('', Elon.as_view(), name='tesla'),
    path('twitter/', Musk.as_view(), name='SpaceX'),
]