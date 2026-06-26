from django.urls import path,include
from members.views import AuthorModelViewSet , GetAllMember , MemberModelViewSet
from books.views import RootLabelBookViewSet, BookModelViewSet , CategoryModelViewSet , ReviewViewSet
from borrows.views import BorrowModelViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register("authors", AuthorModelViewSet)
router.register('books',RootLabelBookViewSet)
router.register('categorys',CategoryModelViewSet)
router.register('members',MemberModelViewSet)
router.register('borrows',BorrowModelViewSet)

author_router = routers.NestedDefaultRouter(router,'authors',lookup="author")
author_router.register('books',BookModelViewSet,basename="author-books")

borrow_router = routers.NestedDefaultRouter(router,'members', lookup="member")
borrow_router.register('borrows',BorrowModelViewSet,basename="member-borrow")

review_router = routers.NestedDefaultRouter(author_router,'books',lookup='book')
review_router.register('reviews',ReviewViewSet , basename="review-books")

urlpatterns = [
    path('',include(router.urls)),
    path('',include(author_router.urls)),
    path('',include(borrow_router.urls)),
    path('',include(review_router.urls))
]
