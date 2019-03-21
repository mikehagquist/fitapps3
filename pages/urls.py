from django.urls import path
from .views import HomeView, AboutView, SugarcutzView, ContactView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('sugarcutz/', SugarcutzView.as_view(), name='sugarcutz'),
    path('contact/', ContactView.as_view(), name='contact'),
]
