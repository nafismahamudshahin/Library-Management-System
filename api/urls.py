from django.urls import path,include
from members.views import AuthorModelViewSet , GetAllMember , MemberModelViewSet
from books.views import RootLabelBookViewSet, BookModelViewSet , CagegoryModelViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register("authors", AuthorModelViewSet)
router.register('books',RootLabelBookViewSet)
router.register('categorys',CagegoryModelViewSet)
router.register('members',MemberModelViewSet)

author_router = routers.NestedDefaultRouter(router,'authors',lookup="author")
author_router.register('books',BookModelViewSet,basename="author-books")


urlpatterns = [
    path('',include(router.urls)),
    path('',include(author_router.urls)),
    # path('members/',GetAllMember.as_view(),name="members"),
]
