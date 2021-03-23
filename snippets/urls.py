from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets.views import UserViewSet, SnippetViewSet


router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
