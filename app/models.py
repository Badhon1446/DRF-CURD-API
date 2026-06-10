from django.db import models

# Create your models here.
class MakeOrder(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=150)
    quantity = models.IntegerField(blank=True, null=True)
    descriptions = models.TextField(blank=True)
    price = models.BigIntegerField()

    def __str__(self):
        return self.name
    
class Review(models.Model):
    order = models.ForeignKey(MakeOrder, on_delete=models.CASCADE, related_name="reviews")
    reviewer = models.CharField(max_length=150)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reviewer

class DeliveryOrder(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, unique=True)
    address = models.TextField(blank= True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name

