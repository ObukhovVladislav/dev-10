from django.db import models
from django_summernote.fields import SummernoteTextField
from datetime import date


class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=128)
    text = SummernoteTextField(verbose_name='Введите текст')
    date = models.DateField(verbose_name='Дата публикации', blank=True, default=date.today)

    def __str__(self):
        return f'{self.title} - {self.date}'

    class Meta:
        ordering = ['-date']
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
