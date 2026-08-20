from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Заголовок",
        help_text="Введите название заголовка"
    )
    content = models.TextField(
        verbose_name="Содержимое",
        help_text="Введите содержимое",
        blank=True,
        null=True,
    )
    preview = models.ImageField(
        upload_to="post/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите изображение",
    )
    creation_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Укажите дату создания",
    )
    publication_status = models.BooleanField(
        default=True
    )
    view_count = models.IntegerField()

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["title"]

    def __str__(self):
        return self.title
