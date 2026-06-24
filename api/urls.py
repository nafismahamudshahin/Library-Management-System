from django.urls import path,include
from members.views import AuthorModelViewSet , GetAllMember
from books.views import BookModelViewSet , CagegoryModelViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register("authors", AuthorModelViewSet)
router.register('books',BookModelViewSet)
router.register('categorys',CagegoryModelViewSet)
# router.register('members',GetAllMember)



urlpatterns = [
    path('',include(router.urls)),
    path('members/',GetAllMember.as_view(),name="members")
]
