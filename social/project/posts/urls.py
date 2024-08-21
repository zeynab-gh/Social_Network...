from django.urls import path
from .views import PostView,PostDetailView,PostCreateView,CommentView,LikeView

urlpatterns =[
    path('posts_list/', PostDetailView.as_view(),name='post'),
    path('post/', PostCreateView.as_view(),name="post"),
    path('post/<int:post_pk>/', PostView.as_view(),name='post'),
    path('post/<int:post_pk>/Comments/', CommentView.as_view(),name='comment'),
    path('post/<int:post_pk>/Likes/', LikeView.as_view(),name='like'),

]