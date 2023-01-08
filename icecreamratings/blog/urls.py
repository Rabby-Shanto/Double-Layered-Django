from django.urls import path
from .import views


urlpatterns = [
    path('list/',views.post_list,name='post_list'),
    path('details/<int:id>',views.detail_post,name='detail')
]
