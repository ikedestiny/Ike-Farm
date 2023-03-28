from django.shortcuts import render, redirect
from django.http import HttpResponse
from livestock.models import order, stock
from livestock.forms import contactUsForm, Customer_order_Form, stockForm

# Create your views here.
def hello(request):
    return render(request,'livestock/hello.html')

def contactUs(request):
    form = contactUsForm()
    if request.method == 'POST':
        form = contactUsForm(request.POST)
        if form.is_valid():
            return redirect('confirmation/')
        else:
            form = contactUsForm()
    return render(request,'livestock/contact.html',{'form':form})

def confirmation(request):
    return render(request,'livestock/confirmation.html')


def make_order(request):
    form = Customer_order_Form()
    if request.method == 'POST':
        form = Customer_order_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmation-page')
        else:
            form = Customer_order_Form()
    return render(request, 'livestock/customer_order.html',{'form':form})

def homepage(request):
    return render(request, 'livestock/homepage.html')

def order_list(request):
    orders = order.objects.all()
    return render(request,'livestock/order_list.html',{'orders':orders})

def order_detail(request,id):
    Order = order.objects.get(id=id)
    return render(request, 'livestock/order_detail.html', {'Order':Order})



def stock_detail(request,id):
    Stock = stock.objects.get(id=id)
    return render(request,'livestock/stock_detail.html',{'Stock':Stock})

def stock_list(request):
    stocks = stock.objects.all()
    return render(request, 'livestock/stock_list.html', {'stocks':stocks})

def add_stock(request):
    form = stockForm()
    if request.method =='POST':
        form = stockForm(request.POST)
        if form.is_valid():
            Stock = form.save()
            
            return redirect('stock-list')
        else:
            form = stockForm()
    return render(request,'livestock/add_stock.html',{'form':form})