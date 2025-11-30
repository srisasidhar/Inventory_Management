from django.contrib import admin, messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from .models import Stock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'reorder_threshold', 'status')
    list_filter = ('is_deleted',)
    actions = ['send_email_alert']

    def status(self, obj):
        return "⚠️ Low Stock" if obj.quantity <= obj.reorder_threshold else "✅ OK"

    @admin.action(description="Send Alert Email to Supplier")
    def send_email_alert(self, request, queryset):
        for stock in queryset:
            send_mail(
                subject=f"Low Stock Alert - {stock.name}",
                message=f"Current stock for {stock.name} is {stock.quantity}. Please reorder soon.",
                from_email="noreply@example.com",
                recipient_list=["supplier@example.com"],
                fail_silently=False,  # Will display errors if any
            )
        self.message_user(request, "Email(s) sent successfully!", level=messages.SUCCESS)
