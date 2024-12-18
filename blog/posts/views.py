from django.shortcuts import render
from django.http import Http404

posts = [
    {
        "id": 1,
        "title": "First Post",
        "content": "This is the first post",
    },
    {
        "id": 2,
        "title": "Second Post",
        "content": "This is the second post",
    },
    {
        "id": 3,
        "title": "Third Post",
        "content": "This is the third post",
    },
]
def home(request):
    return render(request, 'posts/index.html', {'posts': posts})

def post(request, id):
    for post in posts:
        if post["id"] == id:
            return render(request, 'posts/post.html', {'post': post})

    raise Http404()