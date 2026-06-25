from django.urls import path,include
from members.views import AuthorModelViewSet , GetAllMember , MemberModelViewSet
from books.views import RootLabelBookViewSet, BookModelViewSet , CagegoryModelViewSet
from borrows.views import BorrowModelViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register("authors", AuthorModelViewSet)
router.register('books',RootLabelBookViewSet)
router.register('categorys',CagegoryModelViewSet)
router.register('members',MemberModelViewSet)
router.register('borrows',BorrowModelViewSet)

author_router = routers.NestedDefaultRouter(router,'authors',lookup="author")
author_router.register('books',BookModelViewSet,basename="author-books")

borrow_router = routers.NestedDefaultRouter(router,'members', lookup="member")
borrow_router.register('borrows',BorrowModelViewSet,basename="member-borrow")

urlpatterns = [
    path('',include(router.urls)),
    path('',include(author_router.urls)),
    path('',include(borrow_router.urls)),
    # path('members/',GetAllMember.as_view(),name="members"),
]
