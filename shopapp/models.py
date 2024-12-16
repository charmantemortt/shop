from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название магазина")

    def __str__(self):
        return self.name


class Product(models.Model):
    plu = models.CharField(max_length=50, unique=True, verbose_name="PLU товара")
    name = models.CharField(max_length=255, verbose_name="Название товара")

    def __str__(self):
        return f"{self.plu} - {self.name}"


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="stocks", verbose_name="Товар")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="stocks", verbose_name="Магазин")
    quantity_on_shelf = models.PositiveIntegerField(default=0, verbose_name="Количество на полке")
    quantity_in_order = models.PositiveIntegerField(default=0, verbose_name="Количество в заказе")

    class Meta:
        unique_together = ('product', 'shop')

    def __str__(self):
        return f"{self.product.name} в {self.shop.name}"
