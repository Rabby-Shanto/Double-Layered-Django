from django.shortcuts import render


from .models import Post
from django.http import Http404

# Create your views here.


def post_list(request):

    posts = Post.published.all()

    context = {

        'posts' : posts
    }
    return render(request,'post/list_post.html',context)


def detail_post(request,id):

    try:
        post = Post.published.get(id=id)

    except Post.DoesNotExist:

        raise Http404("Post doesn't exists!")

    context = {

        'post' : post
    }

    return render(request,'post/detail.html',context)