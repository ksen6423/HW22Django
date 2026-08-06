from django.core.management.base import BaseCommand
from unicodedata import category

from catalog.models import Product


class Command(BaseCommand):
    help = "Удаляет старые продукты и добавляет тестовые"

    def handle(self, *args, **kwargs):
        # 1. Удаление существующих данных
        self.stdout.write("Очистка базы данных...")
        Product.objects.all().delete()

        # 2. Добавление тестовых данных
        self.stdout.write("Добавление тестовых продуктов...")
        test_products = [
            Product(name="Помидоры", description="Желтые", price=170, category=category),
            Product(
                name="Хлеб",
                description="Ржаной",
                price=70,
                category=category,
            ),
            Product(
                name="Кофе", description="Кофе молотый", price=500, category=category
            ),
        ]

        # Массовое сохранение для скорости
        Product.objects.bulk_create(test_products)

        self.stdout.write(self.style.SUCCESS("База данных успешно обновлена!"))
