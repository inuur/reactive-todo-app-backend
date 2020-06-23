from django.conf import settings
from django.db import models


class List(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    background_image = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=500)
    user_list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='tasks')
    deadline = models.DateField()
    order_num = models.IntegerField()

    def __str__(self):
        return self.title
