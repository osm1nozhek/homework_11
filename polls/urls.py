from django.urls import path

from polls import views

urlpatterns = [
    path("blog/<int:blog_id>", views.blog, name="blog"),
]
