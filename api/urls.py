from django.urls import path,include
from members.views import AuthorModelViewSet
from books.views import BookModelViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register("authors", AuthorModelViewSet)
router.register('books',BookModelViewSet)




urlpatterns = [
    path('',include(router.urls)),
]
