from django.http import Http404
from django.shortcuts import render
from blog.data import posts


# Create your views here.
def blog(request):
    context = {
        "text": "Blog Page Ok !",
        "title": "Blog 📖",
        "poss_class": "content",
        "posts": posts,
    }

    return render(request, "blog/index.html", context)


def post(request, post_id):
    data = None
    for post in posts:
        if post.get("id") == post_id:
            data = post
            break

    if data is None:
        raise Http404('Post não encontrado')

    context = {
        "text": "Blog Page Ok !",
        "title":data["title"],
        "poss_class": "content__post",
        "posts": [data],
    }

    return render(request, "blog/index.html", context)
