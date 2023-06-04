from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='images/%Y/%m/%d', max_length=100, blank=True)
    description = models.CharField( max_length=150, blank=True)
    slug = models.SlugField(max_length = 50)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


class MenuPosition(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField( max_length=150, blank=True)
    price = models.DecimalField( max_digits=5, decimal_places=2)
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%Y/%m/%d', max_length=100, blank=True)    
    
    def __str__(self):
        return self.title
    
class BookedTable(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    datatime_booked = models.DateTimeField(verbose_name='Choose a date.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone = models.TextField()

class SubscriptionContact(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    
    
    
    
                                                               
