from django.urls import path

from .views import HomePageView, AboutPageView, SugarcutzPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('sugarcutz/', SugarcutzPageView.as_view(), name='sugarcutz'),
]
