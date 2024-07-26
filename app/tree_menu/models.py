from django.db import models


class Menu(models.Model):
    title = models.CharField('Название', max_length=128, unique=True)

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField('Название элемента', max_length=128)
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Меню',
    )
    parent_item = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='childrens',
        null=True,
        blank=True,
        verbose_name='Родительский элемент',
    )

    class Meta:
        verbose_name = 'элемент меню'
        verbose_name_plural = 'Элементы меню'

    def __str__(self):
        return self.title
