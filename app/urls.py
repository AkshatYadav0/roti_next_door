from django.urls import path
from . import views

urlpatterns = [
	path("" , views.h1),
	path('l2',views.h2),
	path('l3',views.h3),
	path('home',views.home),
	path('dish/<str:dish_id>',views.dishpage),
	path('cook/<str:cook_no>',views.cookpage),
	path('order/<str:dish_id>',views.order),
	path('order_placed/<str:dish_id>/<int:qty>/<str:cook_name>',views.orderplaced),
	path('post_order_home',views.postorderhome),
	path('track',views.trackorder),
	path('test',views.test),
	path('filter/<str:cat>',views.filter),
	path('pin-filter',views.pinfilter)
]
