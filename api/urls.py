from django.urls import path,include
from rest_framework import routers
from members.views import AuthorModelViewSet
router = routers.DefaultRouter()
router.register("authors", AuthorModelViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
