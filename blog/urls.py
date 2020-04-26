from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('comments/', views.comment_list, name='comment_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/publish_draft_list/', views.post_publish_draft_list, name='post_publish_draft_list'),
    #path('post/<pk>/delete/', views.post_delete, name='post_delete'),
    #path('post/<pk>/delete_draft_list/', views.post_delete_draft_list, name='post_delete_draft_list'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve_redirect/<str:redirect_list>/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/unapprove_redirect/<str:redirect_list>/', views.comment_unapprove, name='comment_unapprove'),
    path('post/<int:postpk>/comment/<int:pk>/delete_redirect/<str:redirect_list>/', views.comment_delete, name='comment_delete'),
    path('post/<int:pk>/delete_redirect/<str:redirect_list>/', views.post_delete_redirect, name='post_delete_redirect'),
]
