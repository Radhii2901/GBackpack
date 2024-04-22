from django.db import models

# Create your models here.

class data(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    femail=models.CharField(max_length=20)
    fcmt=models.CharField(max_length=20)

    def __str__(self):
        return self.fname
    

class sdata(models.Model):
    fnm=models.CharField(max_length=20)
    lnm=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    paswrd=models.CharField(max_length=20)

    def __str__(self):
        return self.fnm    
    

class shopitem(models.Model):
    pname=models.CharField(max_length=20)
    pprice=models.CharField(max_length=10)
    pimage=models.ImageField(upload_to='img') 

    def __str__(self):
        return self.pname
    

class cartitem(models.Model):
    pname=models.CharField(max_length=20)
    pprice=models.CharField(max_length=10)
    pimage=models.ImageField(upload_to='img') 
    ptotal=models.IntegerField(default=50)
    pquantity=models.IntegerField(default=1)

    def __str__(self):
        return self.pname
