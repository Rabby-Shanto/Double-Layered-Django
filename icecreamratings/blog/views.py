from django.shortcuts import render,get_object_or_404


from .models import Post,Comment
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from .forms import EmailSendForm,CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST

# Create your views here.


def post_list(request):

    posts = Post.published.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)

    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts' : posts
    }
    return render(request,'post/list_post.html',context)


def detail_post(request,year,month,day,post):

    try:
        post = Post.published.get(slug=post,publish__year=year,publish__month=month,publish__day=day)
        # List of active comments for this post
        comments = post.comments.filter(active=True)
        # Form for users to comment
        form = CommentForm()

    except Post.DoesNotExist:
        raise Http404("Post doesn't exists!")

    context = {

        'post' : post,
        'comments' : comments,
        'form' : form

    }

    return render(request,'post/detail.html',context)


def send_email(request,post_id):

    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        form = EmailSendForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read " \
            f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
            f"{cd['name']}\'s comments: {cd['message']}"
            send_mail(subject, message, 'django.smtp.host@gmail.com',
            [cd['to_email']])

            sent = True

    else:

        form = EmailSendForm()

    context = {
            'post' : post,
            'form' : form,
            'sent': sent
        }

    return render(request, 'post/share.html',context)


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'post/comments.html',{'post': post,'form': form,'comment': comment})
