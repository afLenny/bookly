from .views import BookView
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'books', BookView, basename='book')

urlpatterns = router.urls
