from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ItemCategory(models.Model):
    category_name = models.CharField(max_length=25, unique= True, blank=False)
    description = models.CharField(max_length= 250, blank= True)

    def __str__(self):
        return self.category_name

class OrderStatus(models.Model):
    status_name = models.CharField(max_length=25, unique= True)
    description = models.CharField(max_length= 250, blank= True)

class MenuItem(models.Model):
    item_name = models.CharField(max_length=25, unique= True)
    description = models.CharField(max_length= 250, blank= True)
    price = models.IntegerField( default= 0)
    item_category = models.ForeignKey(ItemCategory, on_delete=models.PROTECT)

    def __str__(self):
        return self.item_name

class Order(models.Model):
    create_date = models.DateField(auto_now_add= True)
    created_by = models.ForeignKey(User, on_delete= models.PROTECT)
    total = models.IntegerField() # this is a computd field created when the order is requested.
    status = models.ForeignKey(OrderStatus, on_delete= models.CASCADE)

    def __str__(self):
        return self.order
    
class OrderLines(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete= models.PROTECT)
    item_price = models.DecimalField(max_digits= 8, decimal_places= 2) ##  this is a computed field that will be populated from the price column in the menuitem model .
    quantity = models.IntegerField() # this field will be added by the customer at the tome of adding menu_item
    item_total = models.DecimalField(max_digits= 8, decimal_places= 2) # this will be computed my multiplying the item price by the quantity
    order_number = models.ForeignKey(Order, on_delete=models.DO_NOTHING)

    # use to import the price of an item from the MenuItems model
    @property
    def price(self):
        return self.item_price.price
    
    def save(self,*args, **kwargs):
        self.item_price = self.price
        super().save(*args, **kwargs) 

    # this is used to compute the total of 
    @property
    def total(self):
        return self.quantity * self.item_price
    
    def save(self, *args, **kwargs):
        self.item_total = self.total
        super().save(*args, **kwargs)

  ## Cart related Models
class Cart(models.Model):
    cart_id = models.CharField(max_length= 250, blank= True)
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
     cart_item = models.ForeignKey(MenuItem, on_delete= models.CASCADE)
     cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
     quantity = models.IntegerField
     
     def __str__(self):
         return self.cart_item
    