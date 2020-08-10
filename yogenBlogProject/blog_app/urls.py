from django.conf.urls import url
from . import views

urlpatterns = [
    #url('',views.IndexView.as_view(),name='index'),
    url('',views.PostListView.as_view(),name='post_list'),
    url('about/',views.AboutView.as_view(),name='about'),
    url('post/(?P<pk>\d+)',views.PostDetailsView.as_view(),name='post_detail'),
    url('post/new/',views.CreatePostView.as_view(),name='post_new'),
    url('post/edit/(?P<pk>\d+)',views.UpdatePostView.as_view(),name='post_edit'),
    url('post/delete/(?P<pk>\d+)',views.PostDeleteView.as_view(),name='post_delete'),
    url('drafts/',views.DraftListView.as_view(),name='draft_list'),
    url('post/(?P<pk>\d+/comment/)',views.add_comment_to_post,name='add_comment_to_post'),
    url('comment/(?P<pk>\d+/approve/)',views.comment_approve,name='comment_approve'),
    url('comment/(?P<pk>\d+/remove/)',views.comment_remove,name='comment_remove'),
    url('post/(?P<pk>\d+/publish/)',views.post_publish,name='post_publish'),
]