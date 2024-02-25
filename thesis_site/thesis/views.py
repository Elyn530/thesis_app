from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.views.decorators.http import require_POST

from .models import ThesisList, Comment
from .forms import CommentForm


def thesis_list(request):
    post_list = ThesisList.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number) 
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 
                  "thesis/post/list.html",
                  {"posts":posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(ThesisList, 
                             status=ThesisList.ThesisStatus.PUBLISHED,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(active=True)
    form = CommentForm()

    return render(request,
                  "thesis/post/detail.html",
                  {"post":post,
                   "comments": comments,
                   "form":form})
@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(ThesisList, id=post_id, status=ThesisList.ThesisStatus.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    return render(request, "thesis/post/comment.html",
                        {'post': post,
                         'form': form, 
                         'comment': comment})