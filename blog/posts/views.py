from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    html = ""
    for post in posts:
        html += f"""
            <div>
            <a href="/post/{post["id"]}">
                <h1>{post["id"]} - {post["title"]}</h1></a>
                <p>{post["content"]}</p>
            </div>
        """
    return HttpResponse(html)

def post(request, id):
    for post in posts:
        if post["id"] == id:
            return HttpResponse(f"""
                <div>
                    <h1>{post["id"]} - {post["title"]}</h1>
                    <p>{post["content"]}</p>
                </div>
            """)

    return HttpResponseNotFound("<h1>Post not found :(</h1>")

def google(request, id):
    url = reverse("post", args=[id])
    return HttpResponseRedirect(url)