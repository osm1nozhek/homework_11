from django.urls import path

from polls import views

urlpatterns = [
    path("<int:blog_id>", views.publication_read, name="blog"),
]
