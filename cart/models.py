from django.db import models
from app_sportbar.models import MenuPosition
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delivered = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    # total order cost with get_cost() from related Model OrderItem 
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.order_items.all())
    
    def __str__(self):
        return 'Order {}'.format(self.id)
    
    class Meta:
        ordering = ('-created_at',)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(MenuPosition, related_name='products_in_order', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
        

    
    

    