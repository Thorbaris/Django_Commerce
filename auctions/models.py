from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
	watchlist = models.ManyToManyField('product', blank=True)

class Cat(models.Model):
	category = models.CharField(max_length=32)
			
	def __str__(self):
		return f"{self.category}"



class product(models.Model):
	crator = models.CharField(max_length=32, default="Webmaster")
	title = models.CharField(max_length=64)
	description = models.TextField()
	starting_bid = models.CharField(max_length=64)
	img_url = models.CharField(max_length=256, default="unavailable.jpg", null=True)
	categ = models.ForeignKey(Cat, on_delete=models.CASCADE)

	def __str__(self):
		return f"id:{self.id} = {self.title}"

class Comments(models.Model):
	author = models.CharField(max_length=32, default=True)
	onproduct = models.ForeignKey(product, on_delete=models.CASCADE, related_name="comments", default=None)
	content = models.CharField(max_length=256, default="")

	def __str__(self):
		return f"author"

class Bids(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listing = models.ForeignKey(product, on_delete=models.CASCADE, related_name="bids")
    bid = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    timestamp = models.DateTimeField(default=datetime.now())
