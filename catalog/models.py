from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Категория",
        help_text="Введите категорию продукта"
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите изображение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Выберите категорию",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Укажите дату создания",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Укажите дату последнего изменения",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name
