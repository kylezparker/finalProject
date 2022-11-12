from django.urls import path
from .views import HomePageView, AboutPageView, tosView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('termsofservice/', tosView.as_view(), name='tos'),
]