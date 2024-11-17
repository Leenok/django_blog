from django.urls import path
from .views import MainView, AboutView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    # path('contact', ContactView.as_view(), name='contact'),
]