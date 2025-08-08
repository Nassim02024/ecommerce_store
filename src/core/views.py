from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render , redirect
from .models import Product , Category , Vendor , ProductReview ,CartOrder , CartOrderItems
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.


@login_required(login_url='login_view')
def index(request):
  vendor = Vendor.objects.all()
  product = Product.objects.filter(featured=True , product_status="published")
  context = {
    'vendor': vendor,
    'product': product,
  }
  return render(request, 'core/index.html' , context)


def products(request):
  product = Product.objects.filter(product_status="published")
  context = {
    'product': product,
  }
  return render(request, 'core/products.html' , context)

def productsforvendor(request , vid):
  vendor = Vendor.objects.get(vid=vid)
  product = Product.objects.filter(product_status="published" , vendor=vendor)
  context = {
    'product': product,
    'vendor': vendor
  }
  return render(request, 'core/productsforvendor.html' , context)



def category(request , vid):
  vendor = Vendor.objects.get(vid = vid)
  category = Category.objects.filter(vendor=vendor)
  context = {
    'category': category,
    "vendor": vendor
  } 
  return render(request, 'core/category.html' , context)



def product_category(request , cid):
  category = Category.objects.get(cid= cid) # cid is all fields
  product = Product.objects.filter( product_status="published" , category= category)
  context = {
    "category": category,
    "product": product
  } 
  
  return render(request, 'core/product_category.html' , context)



# Dont complete
def vendor(request):
  vendor = Vendor.objects.all()
  context = {
    "vendor": vendor,
  } 
  
  return render(request, 'core/vendor.html' , context)




def productDetils(request , pid):
  productDetils = Product.objects.get(pid= pid)
  products = Product.objects.filter(category= productDetils.category , product_status="published").exclude(pid= pid)
  reviwes = ProductReview.objects.filter(product= productDetils)
  context = {
    "productDetils": productDetils,
    "products": products,
    "reviwes": reviwes,
  
  } 
  
  return render(request, 'core/productDetils.html' , context )



def search_vendor(request):
  query = request.GET.get("q" , "")
  vendor = Vendor.objects.filter(title__icontains=query)
  context = {
    "query": query,
    "vendor": vendor,
    
  
  } 
  
  return render(request, 'core/search_vendor.html' , context )



def search_product(request):
  query = request.GET.get("q" , "")
  product = Product.objects.filter(title__icontains=query)
  context = {
    "query": query,
    "product": product,
    
  
  } 
  
  return render(request, 'core/search_product.html' , context )




from decimal import Decimal
@login_required
def cardorder(request, vid):
    vendor = get_object_or_404(Vendor, vid=vid)
    products = Product.objects.filter(vendor=vendor, product_status="published")

    if request.method == "POST":
        product_ids = request.POST.getlist("product_id[]")
        product_names = request.POST.getlist("productName[]")
        product_prices = request.POST.getlist("price[]")
        qun = request.POST.getlist("qun[]")

        fullname = request.POST.get('fullname')
        email = request.POST.get('email')

        if not (len(product_ids) == len(product_names) == len(product_prices) == len(qun)):
            return HttpResponse("❌ عدد البيانات غير متطابق", status=400)

        # ✅ ننشئ الطلب العام مرة واحدة فقط
        first_product = Product.objects.get(pid=product_ids[0])
        order = CartOrder.objects.create(
            product_name="، ".join(product_names),  # اختياري: عرض أسماء المنتجات مجتمعة
            qunt=sum([int(q) for q in qun]),
            product_price=sum([Decimal(p) for p in product_prices]),
            vendor=vendor,
            product=first_product,  # أو يمكن تركه فارغًا
            user=request.user,
            fullname=fullname,
            email=email,
        )

        # ✅ الآن نضيف كل المنتجات المرتبطة بهذا الطلب
        for pid, name, price, quantity in zip(product_ids, product_names, product_prices, qun):
            try:
                product = Product.objects.get(pid=pid)
            except Product.DoesNotExist:
                continue

            CartOrderItems.objects.create(
                order=order,
                product=product,
                product_status="Processing",
                item=product.title,
                image=product.image.url if product.image else "",
                quantity=int(quantity),
                price=Decimal(price),
                total=Decimal(price) * int(quantity),
                invoice_on=f"INV-{order.id}-{product.pid}",
            )
        send_mail(
          subject = "New Order",
          from_email = email,
          message = f"New Order from {fullname} with order id {order.id} and total price {order.product_price}",
          recipient_list=["blingohyper@gmail.com"]
        )
        return HttpResponse("✅ تم إنشاء الطلب بكافة العناصر بنجاح")

    context = {
        "vendor": vendor,
        "product": products,
    }
    return render(request, "core/cardorder.html", context)