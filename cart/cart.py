from decimal import Decimal
from django.conf import settings
from app_sportbar.models import MenuPosition


class Cart(object):

    def __init__(self, request):
        # current session
        self.session = request.session

        # session cart
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart
        # self.cart - (dict{
        # {'product_id1':{'product_attribute1': product_value1},
        # {'product_id2':{'product_attribute2': product_value2}
        # })

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)

        # freeze the current price
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
            # with 'price': product.price raise an error "object Decimal is not Json serializable
            'price': str(product.price)}
        
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            # by default update_quantity=False so chiefly the next goes
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # update session. it's a dict now
        self.session[settings.CART_SESSION_ID] = self.cart
        # addin flag modified to the session
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        # getting products from model
        products = MenuPosition.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
            # so now a Cart instance is iterable as iteration of self.cart.values() adding new keys:values
            # for item in  cart_instance:
 
    def __len__(self):
        # getting number of products
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_cost(self):
    # the cart total cost
        return sum(Decimal(item['price']) * item['quantity'] for item in
               self.cart.values())
    
    def clear(self):
        # delete the cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
