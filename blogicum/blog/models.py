from django.db import models
from django.contrib.auth import get_user_model

from core.models import BaseModel, TitleModel


User = get_user_model()


class Location(BaseModel):
    """Локация."""

    name = models.CharField(max_length=256, verbose_name='Название места')

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Category(BaseModel, TitleModel):
    """Категория."""

    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        unique=True, verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; разрешены \
символы латиницы, цифры, дефис и подчёркивание.'
    )
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Post(BaseModel, TitleModel):
    """Пост."""

    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем\
 — можно делать отложенные публикации.'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Местоположение',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
