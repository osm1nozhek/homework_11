from django.db import models


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)
