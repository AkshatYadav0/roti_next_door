from django.contrib import admin

# Register your models here.
from . models import Customer, Dishe, Cook, Order, KitchenImage, Categories

admin.site.register(Customer)
admin.site.register(Dishe)
admin.site.register(Order)
admin.site.register(Categories)
 
class ImageAdmin(admin.StackedInline):
	model = KitchenImage
 
@admin.register(Cook)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]
 
    class Meta:
       model = KitchenImage
 
@admin.register(KitchenImage)
class ImageAdmin(admin.ModelAdmin):
    pass