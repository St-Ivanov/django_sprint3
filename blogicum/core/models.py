from django.db import models


class BaseModel(models.Model):
    """Базовая модель."""

    is_published = models.BooleanField(
        default=True, 
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.',
                                       )
    created_at = models.DateTimeField(
        verbose_name='Добавлено',
        auto_now_add=True,
    )

    class Meta:
        abstract = True


class TitleModel(models.Model):
    """Заголовок модель."""

    title = models.CharField(max_length=256, verbose_name='Заголовок')

    class Meta:
        abstract = True
