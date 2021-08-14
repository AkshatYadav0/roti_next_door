from django.db import models

# Create your models here.

class Customer(models.Model):
	Name  	 	 = models.CharField(max_length = 100)
	Order_ID 	 = models.CharField(max_length = 100, unique=True)
	Mobile 		 = models.CharField(max_length=13)
	Address 	 = models.TextField()
	Instructions = models.TextField()

	def __str__(self):

		return ''+self.Name +  ' || Order_ID: ' + '['+self.Order_ID+']'



class Cook(models.Model):
	def jsonfield_default_value():
		return dict(zip(['Twitter', 'Instagram'],["/twitter.com/ID", "/instagram.com/ID"]))
	cookName				= models.CharField(max_length=100)
	cookNumber				= models.CharField(max_length=13)
	kitchenName				= models.CharField(max_length=100)
	aboutCook				= models.TextField()
	servingSince			= models.CharField(max_length=100)
	ordersServedTillDate	= models.CharField(max_length=100)
	hasFSSAI 				= models.BooleanField()
	cookPhoto				= models.ImageField(upload_to = 'images/')
	ingredientQualityUsed	= models.CharField(max_length=100)
	cookAddress				= models.TextField()
	social 					= models.JSONField(default=jsonfield_default_value)
	def __str__(self):

		return 'Name: '+self.cookName +  ' || Cook Number: ' + '['+self.cookNumber+']'



class KitchenImage(models.Model):
	cook   = models.ForeignKey(Cook, on_delete=models.CASCADE,related_name='cooks')
	images = models.FileField(upload_to = 'images/')

	def __str__(self):

		return 'COOK: '+self.cook.cookName +  ' || Cook Number: ' + '['+self.cook.cookNumber+']'

class Categories(models.Model):
	pop_categroy_name = models.CharField(max_length=100,null=False)
	photo 			  = models.ImageField(upload_to = 'images/')
	def __str__(self):
		return 'Popular Category: '+self.pop_categroy_name 

class Dishe(models.Model):
	def jsonfield_default_value():
		return [" ", " "]
	categories          = models.ForeignKey(Categories,on_delete=models.CASCADE)
	dishID 				= models.CharField(max_length=100, unique = True)
	dishName 			= models.CharField(max_length=100)
	dishPrice 			= models.IntegerField()
	dishDescription 	= models.TextField()
	deliveryTime 		= models.CharField(max_length=100)#DurationField()#
	dishIngredients 	= models.JSONField(default=jsonfield_default_value)
	servesHowMany 		= models.IntegerField()
	pincode             = models.IntegerField()
	approxDeliveryCost  = models.CharField(max_length=100)
	dishPhotos 			= models.ImageField(upload_to = 'images/')
	cook 				= models.ForeignKey(Cook, on_delete=models.CASCADE)
	def __str__(self):
		return 'Dish_ID: '+self.dishID +  ' || Dish Name: ' + '['+self.dishName+']'



class Order(models.Model):
	Qty 		= models.IntegerField()
	Order_ID 	= models.CharField(max_length=100, unique =True)
	Name 		= models.CharField(max_length=100)
	Mobile 		= models.CharField(max_length=13)
	Address 	= models.TextField()
	cookName	= models.CharField(max_length=100)
	dishID		= models.CharField(max_length=100)

	def __str__(self):

		return 'Name: '+self.Name +  ' || Order_ID: ' + '['+self.Order_ID+']'