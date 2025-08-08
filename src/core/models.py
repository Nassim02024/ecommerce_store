from django.db import models
import uuid 
from django.utils.html import mark_safe
from users.models import User



status_choices = (
  ("process" , "Processing"),
  ("shipped" , "Shipped"),
  ("delivered" , "Delivered"),
)

status = (
  ("draft" , "Draft"),
  ("disabled" , "Disabled"),
  ("rejected" , "Rejected"),
  ("in_review" , "In_review"),
  ("published" , "Published"),
)
stock = (
  ("yes" , "yes"),
  ("no" , "no"),
)


rating = (
  (1 , "⭐✰✰✰✰"),
  (2 , "⭐⭐✰✰✰"),
  (3 , "⭐⭐⭐✰✰"),
  (4 , "⭐⭐⭐⭐✰"),
  (5 , "⭐⭐⭐⭐⭐"),
)


titlecategory = (
  ("men" , "men"),
  ("food" , "food"),
  ("women" , "women"),
  ("kids" , "kids"),
  ("accessories" , "accessories"),
  ("shoes" , "shoes"),
  ("bags" , "bags"),
  ("jewelry" , "jewelry"),
  ("home" , "home"),
  ("beauty" , "beauty"),
)
def user_directory_path(instans , filename):
  return 'user_{0}/{1}'.format(instans.user.id , filename)

class Category(models.Model):
  cid = models.UUIDField( unique=True , default=uuid.uuid4 , editable=False ) #unique mean Dont Repeat
  vendor = models.ForeignKey("Vendor", on_delete=models.CASCADE, null=True, blank=True, related_name="VendorCategories")
  
  categoress = models.CharField(max_length=100 , choices=titlecategory , default="men") 
  descreption = models.CharField(max_length=100 ) 
  imge = models.ImageField(upload_to='category')
     
  class Meta:
    verbose_name_plural = 'Category'
    
  def Category_imge(self):
    return mark_safe("<img src='%s' width='50' height='50' />" % (self.imge.url))  
  
  def __str__(self):
    return self.categoress

class Vendor(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  vid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
  
  
  title = models.CharField(max_length=100)
  image = models.ImageField(upload_to=user_directory_path)  
  description = models.TextField(null= True , blank=True) #blank mean can this input in form is empty
  address = models.CharField(max_length=100 , null=False , blank=False)
  contact = models.CharField(max_length=15 , default="+213 ")
  time_response = models.CharField(max_length=100 , null=True , blank=True)
  shipping_on_time = models.CharField(max_length=100 , null=True , blank=True)
  days_to_return = models.CharField(max_length=100 , null=False , blank=False)
  warranty = models.CharField(max_length=100 , null=True , blank=True) # Garantie(الضمان)
  
  
  class Meta:
    verbose_name_plural = "Vendor"
    
  def __str__(self):
    return self.title 
    
  def Vendor_image(self):
    return mark_safe("<img src='%s' width='50' height='50' />" % (self.image.url))
      

class tags(models.Model):
  pass      
class Product(models.Model):
  pid = models.UUIDField(unique=True , default=uuid.uuid4 , editable=False)
  vendor = models.ForeignKey(Vendor , on_delete=models.SET_NULL , null=True , related_name='vendor')
    
  category = models.ForeignKey(Category , on_delete=models.SET_NULL , null=True , related_name="Category" )
  title = models.CharField(max_length=100)
  image = models.ImageField(upload_to=user_directory_path , default="product.jpg")  
  description = models.TextField(max_length=300 ,  null= True , blank=True)
  color = models.CharField(max_length=300 ,  null= True , blank=True)
  price = models.DecimalField(max_digits=999, decimal_places=2 )
  old_price = models.DecimalField(max_digits=999 , decimal_places=2 )
  in_stock = models.CharField(choices=stock , default="yes" ) # mean how many product in stock without "decimal_places(.)"
  specifications = models.TextField(null=True , blank=True , max_length=300)
  # tags = models.ForeignKey(tags , on_delete=models.SET_NULL , null=True)
  product_status = models.CharField(choices=status , max_length=10 , default="published")
  status = models.BooleanField(default=True)
  featured = models.BooleanField(default=False) # المنتج مميز  
  digital = models.BooleanField(default=False) 
  sku = models.CharField(max_length=200 , default=uuid.uuid4 , editable=False) 
  date = models.DateField(auto_now_add=True)
  update = models.DateTimeField(auto_now=True)
  
  
  user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True )
  class Meta:
    verbose_name_plural = "Product"
    
  def __str__(self):
    return self.title
    
  def product_image(self):
    return mark_safe("<img src='%s' width='50' height='50' />" % (self.image.url))
    
  def get_precentage(self):
    new_price = (self.price / self.old_price) * 100
    return new_price
  
  # tags = models.ForeignKey(tags , on_delete=models.SET_NULL , null=True , blank=True)
  # user = models.ForeignKey(User , on_delete=models.CASCADE)
  # category = models.ForeignKey(category , on_delete=models.CASCADE)


class Imgs_product(models.Model):
  images = models.ImageField(upload_to="product-images" , default="product.jpg")
  product = models.ForeignKey(Product , on_delete=models.SET_NULL , null=True)
  date = models.DateField(auto_now_add=True)
  
  class Meta:
    verbose_name_plural = "Product Images"
    
    




##################################### cartOrder , cartOrderItems ############################################################



class CartOrder(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  product = models.ForeignKey(Product , on_delete=models.CASCADE  , null=True , blank= True)
  vendor = models.ForeignKey(Vendor , on_delete=models.CASCADE   , null=True , blank= True)
  
  fullname = models.CharField(max_length=100 , blank=True, null=True)
  email = models.CharField(max_length=100 , blank=True, null=True)
  customer_name = models.CharField(max_length=200)
  product_name =  models.CharField(max_length=200)
  product_price = models.DecimalField(max_digits=10, decimal_places=2 , blank=True, null=True)
  qunt = models.IntegerField()
  paid_status = models.BooleanField(default=False) # means that the order is paid(تم الدفع او لا )
  order_date = models.DateField(auto_now_add=True)
  product_status = models.CharField(choices=status_choices , max_length=30 , default="Processing")


  class Meta:
    verbose_name_plural = "Cart Order"

  def __str__(self):
    return f"{self.customer_name} - {self.product_name} - {self.product_price}"
  

class CartOrderItems(models.Model):
  invoice_on = models.CharField(max_length=300 )
  order = models.ForeignKey(CartOrder , on_delete=models.CASCADE , related_name="items")
  product = models.ForeignKey(Product , on_delete=models.CASCADE)
  
  product_status = models.CharField(max_length=300 )
  item = models.CharField(max_length=300 )
  image = models.CharField(max_length=300 )
  quantity = models.IntegerField(default=0)
  price = models.DecimalField(max_digits=999 , decimal_places=2)
  total = models.DecimalField(max_digits=999 , decimal_places=2)
  
  class Meta:
    verbose_name_plural = "Cart Order Items"

  def order_img(self):
    return mark_safe("<img src='/media/%s' width='50' height='50' />" % (self.image))




##################################### Prodact Review ############################################################



class ProductReview(models.Model):
  user = models.ForeignKey(User  , on_delete=models.CASCADE)
  product = models.ForeignKey(Product  , on_delete=models.CASCADE , related_name="reviwes") # related_name="reviwes" mean from product we can get reviwes
  review = models.TextField()
  rating = models.CharField(choices=rating )
  date = models.DateField(auto_now_add=True)


  class Meta:
    verbose_name_plural = "product Review"
  
  def __str__(self):
    return self.product.title
  
  def get_absolute_url(self):
    return self.rating
  



class Wishlist(models.Model):
  user = models.ForeignKey(User  , on_delete=models.SET_NULL , null=True , blank=True)
  product = models.ForeignKey(Product  , on_delete=models.CASCADE)
  date = models.DateField(auto_now_add=True)


  class Meta:
    verbose_name_plural = "wishlist"
  
  def __str__(self):
    return self.product.title


class Address(models.Model):
  user = models.ForeignKey(User  , on_delete=models.SET_NULL , null=True , blank=True)
  address = models.CharField(max_length=100 , null=True , blank=True)
  status = models.BooleanField(default=False)
  
  class Meta:
    verbose_name_plural = "address"
  




