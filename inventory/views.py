from django.shortcuts import render
from .models import Stock

def home(request):
    return render(request, 'inventory/home.html')

def stock_list(request):
    stocks = Stock.objects.filter(is_deleted=False)
    return render(request, 'inventory/stock_list.html', {'stocks': stocks}) 
def send_stock_alert(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)

    send_mail(
        subject=f"Low Stock Alert: {stock.name}",
        message=f"The stock for {stock.name} is now only {stock.quantity}. Please reorder soon.",
        from_email="noreply@example.com",
        recipient_list=["supplier@example.com"],
        fail_silently=False
    )
    
    return redirect('/admin/inventory/stock/')


