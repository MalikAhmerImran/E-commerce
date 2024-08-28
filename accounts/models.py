from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None,password2=None,is_owner=False):
        if not username:
            raise ValueError("The Username field is required")
        if not email:
            raise ValueError("The Email field is required")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,is_owner=is_owner)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, password=None):
        user = self.create_user(username=username, email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
    
class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=6,null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects=UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    
class Store(models.Model):
    store_name=models.CharField(max_length=255)
    store_address=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)


class Member(models.Model):
    member_name=models.CharField(max_length=255)
    member_email=models.EmailField()
    is_owner=models.BooleanField(default=False)
    is_employe=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)
    user=models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)  

class StoreMember(models.Model):
    store=models.ForeignKey(Store,related_name='store',on_delete=models.CASCADE)
    member=models.ForeignKey(Member,related_name='member',on_delete=models.CASCADE)  

class Product(models.Model):
    product_name=models.CharField(max_length=255,unique=True)
    product_price=models.PositiveIntegerField()
    user=models.ForeignKey(User,related_name='products',on_delete=models.CASCADE)


    def __str__(self):
        return self.product_name
    
class Order(models.Model):

    customer_contact=models.CharField(max_length=12)
    customer_address=models.CharField(max_length=255)
    date=models.DateTimeField(auto_now_add=True)
    is_approved=models.BooleanField(default=False)
    order_by=models.ForeignKey(User,on_delete=models.CASCADE)
    
    
class OrderDetails(models.Model):
    order=models.ForeignKey(Order,related_name='products',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()

class Images(models.Model):
    image=models.FileField(upload_to='product_pictures/')
    caption=models.CharField(max_length=255)
    product=models.ForeignKey(Product,related_name='product_images',on_delete=models.CASCADE)







