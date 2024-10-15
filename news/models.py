from django.db import models

from users.models import User


class News(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='news_images')


    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'


    def __str__(self):
        return f'title: {self.title}'

class Comment(models.Model):
    news = models.ForeignKey(News, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Измените это поле
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
