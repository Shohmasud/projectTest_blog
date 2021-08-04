from django.urls import path
from .views import PostListView, PostDeleteView, PostListCommentView,SerializerComments,SerializerBlogShow,SerializerCommentsCreate,SerializerBlogCreate

urlpatterns = [
    # url
    path('blog/show', PostListView.as_view(), name='post-list'),
    path('comment/delete/<int:pk>', PostDeleteView.as_view(), name='post-delete'),
    path('comment/create/<int:pk>', PostListCommentView.as_view(), name='post-parent'),

    # /// Rest Api
    # GET
    path('get/api/v6/comments/', SerializerComments.as_view()),
    path('get/api/v6/create/blog/show/', SerializerBlogShow.as_view()),
    # Post
    path('post/api/v6/create/comments/', SerializerCommentsCreate.as_view()),
    path('post/api/v6/create/blog/', SerializerBlogCreate.as_view()),]
