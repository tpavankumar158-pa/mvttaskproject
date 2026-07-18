from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import Product
from myapp.forms import ProductForm
# Create your views here.
def addproduct(request):
    pform = ProductForm()
    if request.method == 'POST':
        pform = ProductForm(request.POST)
        if pform.is_valid():
            pform.save(commit=True)
            return redirect('/')
    return render(request,'myapp/add.html',{'form':pform}) 

def getproducts(request):
    products = Product.objects.all()
    return render(request,'myapp/products.html',{'PrdList':products})   
     
def getproduct(request):
    pid=request.GET.get('id')
    product = get_object_or_404(Product,ProductId=pid)
    return render(request,'myapp/find.html',{'prds':product})

def editproduct(request,id):
    product = get_object_or_404(Product,ProductId=id)
    pform = ProductForm(instance=product)
    if request.method=='POST':
        pform = ProductForm(request.POST,instance=product)
        if pform.is_valid():
            pform.save()
            return redirect('/')
    return render(request,'myapp/edit.html',{'form':pform})

def deleteproduct(request,id):
    product = get_object_or_404(Product,ProductId=id)
    if request.method =="POST":
        product.delete()
        return redirect('/')
    return render(request,'myapp/delete.html',{'prds':product})