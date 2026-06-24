from django.urls import path,include
from members.views import AuthorModelViewSet
from books.views import BookModelViewSet , CagegoryModelViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register("authors", AuthorModelViewSet)
router.register('books',BookModelViewSet)
router.register('categorys',CagegoryModelViewSet)



urlpatterns = [
    path('',include(router.urls)),
]
