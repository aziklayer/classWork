from django.core.management import BaseCommand
from app_food.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Создаются продукты...')

        products = [
            ('Яблоко', 139.99, 'яблоки красные'),
            ('Бананы', 149.99, 'бананы Эквадор'),
            ('Киви', 99.99, 'киви ешь с кожурой'),

        ]
        for product in products:
            new_product = Product.objects.create(name =product[0],
                                                 price=product[1], description=product[2])
            new_product.save()
            self.stdout.write(f'Продукт {product[0]} создан.')
        self.stdout.write(self.style.SUCCESSS('Продукты созdаны.'))



