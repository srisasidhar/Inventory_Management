from django.db import models
from inventory.models import Stock

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class PurchaseBill(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    bill_number = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Bill #{self.bill_number} - {self.supplier.name}"


class PurchaseItem(models.Model):
    purchase_bill = models.ForeignKey(PurchaseBill, on_delete=models.CASCADE)
    item = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.item.name} (x{self.quantity})"
