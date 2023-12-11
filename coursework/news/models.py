from datetime import datetime

from django.db import models


# Create your models here.

class abastractArticle(models.Model):
    title = models.CharField('Название', max_length=50, default='')
    anons = models.CharField('Анонс', max_length=255)
    full_text = models.TextField('Статья')
    date = models.DateTimeField(verbose_name='Дата публикации', default=datetime.now)
    img_url = models.TextField('Ссылка на картинку', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class CheckArticles(abastractArticle):

    def get_absolute_url(self):
        return f'/news/check'

    class Meta:
        verbose_name = 'Предложенная новость'
        verbose_name_plural = 'Предложенные новости'


class Articles(abastractArticle):

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
