from django.urls import path
from .import views


urlpatterns = [
    path('list/', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.detail_post, name='detail'),
    path('<int:post_id>/share/', views.send_email, name='send_email'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag')
]
