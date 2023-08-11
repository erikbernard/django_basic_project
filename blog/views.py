from random import randint
from django.http import Http404
from django.shortcuts import render
from blog.data import posts


# Create your views here.
def blog(request):
    date = ['Jan','Fev', 'Nov', 'Abr', 'Mar', 'Ago','Dez']
    usename = ['Jose Nilto', 'Michael wick', 'Victo Nort', 'Aisha Niru', 'Naruto Uzumaki','Sasha Oroch', 'Fith Nekli']
    for post in posts:
        index_img = randint(1,6)
        day =randint(1,30)
        post['image'] = f'images/post_{index_img}.png'
        post['date'] = f'{day} {date[index_img]} 2022'
        post['username'] = usename[index_img]


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
