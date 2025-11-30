from django.db import models
from inventory.models import Stock

class SaleBill(models.Model):
    customer_name = models.CharField(max_length=200)
    bill_number = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Sale #{self.bill_number} - {self.customer_name}"


class SaleItem(models.Model):
    sale_bill = models.ForeignKey(SaleBill, on_delete=models.CASCADE)
    item = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.item.name} (x{self.quantity})"
