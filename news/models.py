from datetime import datetime
from django.db import models


class News(models.Model):
    title: str = models.CharField(max_length=270, verbose_name='Наіменування')
    content: str = models.TextField(blank=True, verbose_name='Контент')
    created_at: datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at: datetime = models.DateTimeField(auto_now=True, verbose_name='Оновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубліковано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, default=1,
                                 verbose_name='Категорія')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=270, db_index=True, verbose_name='Наіменування категорії')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']
