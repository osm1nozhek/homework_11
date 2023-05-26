from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from polls.models import Blog


# Create your views here.
@cache_page(60 * 15)
def publication_read(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        message = (
            f"<h1>Publication with ID: {blog_id} doesn't exist. Try another ID!</h1>"
        )
        return HttpResponse(message)
    return render(request, "blog.html", {"blog": blog})
