from django.db import models


# Create your models here.


class News(models.Model):
    name = models.CharField('Статья', max_length=120, null=False)
    description = models.TextField()
    tags = models.CharField(max_length=30)
    tag_news = models.CharField(max_length=20)
    date = models.DateField(auto_now=False)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'{self.name}'
