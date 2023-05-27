from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from polls.models import Blog


# Create your views here.
@cache_page(60 * 15)
def blog(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        message = " Try another ID!"
        return HttpResponse(message)

    return render(request, "blog.html", {"blog": blog})
