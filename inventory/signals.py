from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Stock

@receiver(post_save, sender=Stock)
def check_low_stock(sender, instance, **kwargs):
    if instance.quantity <= instance.reorder_threshold and not instance.is_deleted:
        subject = f"Low Stock Alert: {instance.name}"
        message = f"""
        The stock for {instance.name} has dropped to {instance.quantity}.
        Please reorder soon. (Threshold: {instance.reorder_threshold})
        """
        send_mail(
            subject,
            message,
            "admin@inventory.com",  # from
            ["your_email@gmail.com"],  # to
            fail_silently=True,
        )
