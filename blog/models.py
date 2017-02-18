import datetime


from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField('')


class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


admin.site.register(BlogsPost, BlogsPostAdmin)

# flows is unuseful
'''def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text'''
