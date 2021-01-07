from django.db import models
from django.urls import reverse
from  accounts.models import User



class Categories(models.Model):
    sub_category=models.ForeignKey('self',on_delete=models.CASCADE,related_name='scategory',null=True,blank=True)
    is_sub = models.BooleanField(default=False)
    name= models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural='categroies'


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('shop:category_filter',args=[self.slug,])




class Product(models.Model):
    category= models.ManyToManyField(Categories,related_name='products')
    name = models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True)
    image=models.ImageField(upload_to='products/%Y/%m/%d/')
    discription = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.slug,])


class Comment(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE,null= True,related_name='ucomment')
    product =models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='pcomment')
    created = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank =True,related_name='rcomment')
    is_reply=models.BooleanField(default=False)
    body=models.TextField(max_length=400,null=True)


    class Meta:
        ordering =('created',)

    def __str__(self):
        return f'{self.user}----{self.body}'
