import uuid
from django.contrib   import  auth
from django.http      import  JsonResponse
from django.contrib   import  messages
from django.shortcuts import  render, get_object_or_404, redirect

from . models import Customer, Dishe, Cook, Order, KitchenImage, Categories

def test(request):
	return render(request,"Home-V0/i.html")

def h1 (request):
	return render(request,"Loader1/index.html")

def h2 (request):
	return render(request,"Loader2/index.html")

def h3 (request):
	return render(request,"Loader3/index.html")

def home (request):
	allpin  =   Dishe.objects.values_list()
	pincode =   []
	for i in range(len(allpin)):
		pincode.append(allpin[i][-4])
	allcat  =   Categories.objects.all()
	alldish = 	Dishe.objects.filter(categories=allcat[0])
	params  =   {'allpin':set(pincode),'alldish':alldish,'cat':allcat}
	return render(request,"Home-V0/i.html",context=params)

def filter(request,cat):
	cat	 =	get_object_or_404(Categories,pop_categroy_name=cat)
	dish =  Dishe.objects.filter(categories=cat).values()
	cook = []
	k = len(dish)
	for i in range(k):
		cook.append(list(Cook.objects.filter(pk=dish[i]['cook_id']).values()))
	return JsonResponse({'dish':list(dish),'cook':list(cook)})

def dishpage(request,dish_id):
	dish  		= 	Dishe.objects.get(dishID = dish_id)
	params  	=   {'dish':dish}
	return render(request,"Dish Page/index.html",context=params)

def cookpage(request,cook_no):
	cook 		=   get_object_or_404(Cook, cookNumber=cook_no)
	image  		= 	KitchenImage.objects.filter(cook=cook)
	params  	=   {'cook':cook,'image':image}
	return render(request,"CookPage/index.html",context=params)

def order(request,dish_id):
	dish 		=   Dishe.objects.get(dishID = dish_id)
	if request.method == 'POST':
		qty 		= request.POST.get('qty')
	params  	=   {'dish':dish,'qty':qty}
	return render(request,"UserInput/index.html",context=params)

def orderplaced(request,dish_id,cook_name,qty):
	if request.method ==  'POST':
		name          =    request.POST.get('name')
		mobile        =    request.POST.get('mobile')
		address       =    request.POST.get('address')
		instructions  =    request.POST.get('instructions')
		count         =    Order.objects.all().count()

		if((mobile.split(' ')[-1]).replace("+","").isdigit() != True or len((mobile.split(' ')[-1]).replace("+","")) != 10):
			messages.error(request,"Enter a valid Mobile Number")
			dish 		=   Dishe.objects.get(dishID = dish_id)
			params  	=   {'dish':dish}

			return render(request,"UserInput/index.html",context=params)
		
		elif(name == '' or mobile == '' or address == ''):
			messages.error(request,"Please fill the required correctly")
			dish 		=   Dishe.objects.get(dishID = dish_id)
			params  	=   {'dish':dish}

			return render(request,"UserInput/index.html",context=params)

		else:
			customer_id   =    1000+count+1 #uuid.uuid4()
			if(Order.objects.filter(Order_ID = customer_id).count() == 1):
				customer_id +=1
				print("-------------------------1----------------------------------")
				Order.objects.filter(QTY=qty, Order_ID = customer_id).update(Name=name,Order_ID=customer_id,
					Mobile=mobile,Address=address,cookName=cook_name,dishID=dish_id)
				print("-------------------------2----------------------------------")
				Customer.objects.filter(Order_ID = customer_id).update(Name=name,Order_ID=customer_id,
					Mobile=mobile,Address=address,Instructions=instructions)
				print("-------------------------3----------------------------------")
			else:
				customer      =    Customer(Name=name,Order_ID=customer_id,Mobile=mobile,
					Address=address,Instructions=instructions)

				order 		  =    Order(Qty=qty, Name=name,Order_ID=customer_id,Mobile=mobile,
					Address=address,cookName=cook_name,dishID=dish_id)
				customer.save()
				order.save()
			return render(request,"OrderConfirmation/index.html")

def postorderhome(request):
	allpin  =   Dishe.objects.values_list()
	pincode =   []
	for i in range(len(allpin)):
		pincode.append(allpin[i][-4])
	allcat  =   Categories.objects.all()
	alldish = 	Dishe.objects.filter(categories=allcat[0])
	params  =   {'allpin':set(pincode),'alldish':alldish,'cat':allcat}
	return render(request,"PostOrderhome/i.html",context=params)

def trackorder(request):
	return render(request,"OrderTracking/index.html")

def pinfilter(request):
	allpin  =   Dishe.objects.values_list()
	pincode =   []
	for i in range(len(allpin)):
		pincode.append(allpin[i][-4])
	allcat  = Categories.objects.all()
	query   = request.GET['search']
	alldish = Dishe.objects.filter(pincode = query,categories=allcat[0])
	params  = {'allpin':set(pincode),'alldish':alldish,'cat':allcat}	
	return render(request,"Pin-Filter/i.html",context=params)