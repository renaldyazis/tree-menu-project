from django.db import models
from django.urls import reverse, NoReverseMatch


class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название пункта")
    url = models.CharField(
        max_length=255,
        blank=True,
        help_text="URL или именованный URL-шаблон (например: 'product_list' или '/products/')"
    )
    named_url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Именованный URL",
        help_text="Имя path из urls.py (приоритет над полем URL)"
    )
    menu_name = models.CharField(max_length=50, verbose_name="Название меню")
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children'
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        ordering = ['order']
        unique_together = ['menu_name', 'url', 'named_url']
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return self.url or "#"
        return self.url or "#"
