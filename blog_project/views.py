from django.shortcuts import get_object_or_404, render
from blog_project.models import Post, Comment
from django.http import HttpResponseRedirect
from blog_project.forms import CommentForm


# Create your views here.

# this is post view setup to display list of all posts

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html",context)

# blog_category is category view setu, posts will be shown only be of specific category that the user choose

def  blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains = category
    ).order_by("-created_on")
    context = {
        "category" : category,
        "posts" : posts,
    }
    return render(request, "blog/category.html", context)

# blog_detail() will display the full post . later this view will also show exiting comments and a textarea(form) to allow users to create new comments

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post" : post,
        "comments" : comments,
        "form": CommentForm(),
    }
    return render(request, "blog/details.html",context)