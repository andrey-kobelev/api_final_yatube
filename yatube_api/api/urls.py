from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(
    prefix=r'posts', viewset=PostViewSet, basename='posts'
)
router_v1.register(
    prefix=r'posts/(?P<post_id>\d+)/comments',
    viewset=CommentViewSet,
    basename='comments'
)
router_v1.register(prefix='follow', viewset=FollowViewSet, basename='follow')
router_v1.register(prefix='groups', viewset=GroupViewSet, basename='groups')
urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt'))
]
