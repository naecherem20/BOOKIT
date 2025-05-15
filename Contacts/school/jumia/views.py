from django.shortcuts import render
from .models import Product ,Category


# Create your views here.
def shopping(request):
    items=Product.objects.all()
    return render(request,'jumia/shop.html',{'Product':items})

def product(request,pk):
    items=Product.objects.get(id=pk)
    return render(request,'jumia/product.html',{'Product':items})

def about(request):
    print("this is the about")
    return render(request,'jumia/about.html')


def categorise(request,imems):
    print(imems)
    category= Category.objects.get(title=imems)
    print(category)
    items= Product.objects.filter(category=category)
    print(items)
    #replace hyphen with spaces
    #imems=imems.replace("-"," ")
    #print(imems)
    #try:
        #look up category
        #category= Category.objects.get(title=imems)
        #items= Product.objects.filter(category=category)  
    return render(request,'jumia/category.html',{'items':items,'name':"Perpetual"})
    #except:
     #   return render(request,'student.html',{'items':items})

