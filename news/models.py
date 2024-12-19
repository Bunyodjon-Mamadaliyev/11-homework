from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


class News(models.Model):
    title = models.CharField(max_length=200)
    short_content = models.TextField()
    long_content = models.TextField()
    category = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100, default='Unknown')


    class Meta:
        verbose_name_plural = 'News'

    def get_detail_url(self):
        return reverse('news:detail', args=[self.pk])