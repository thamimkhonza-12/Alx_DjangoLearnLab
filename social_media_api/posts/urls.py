from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path
from .views import FeedView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),

    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),

]


router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)



urlpatterns = router.urls



