from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=150)
    quantity = models.IntegerField(default=0)
    reorder_threshold = models.IntegerField(default=10)  # New field
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
