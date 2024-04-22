from django.http import JsonResponse
from django.shortcuts import render , redirect

from myapp.models import *

# Create your views here.



def first(request):
    return render(request,'index.html')

def second(request):
    return render(request,'contact.html')

def third(request):
    return render(request,'login.html')

def sign(request):
    return render(request,'signup.html')

def cart(request):
    obj2=cartitem.objects.all()
    return render(request,'cart.html',{'cart':obj2})

def shopnow(request):
    obj=shopitem.objects.all()
    return render(request,'shop.html',{'item':obj})


def blogg(request):
    return render(request,'blog.html')
def pett(request):
    return render(request,'pet.html')   

def storedata(reqest):
    l=reqest.GET['a']
    m=reqest.GET['b']
    n=reqest.GET['c']
    o=reqest.GET['d']

    obj=data(fname=l,lname=m,femail=n,fcmt=o)
    obj.save()
    return redirect('')


def lgdata(request):
    s=request.GET['nm']
    t=request.GET['psw']

    obj=sdata.objects.all()
    
    for i in obj:
        if i.fnm==s and i.paswrd==t:
            return redirect('/home')
    return redirect('/login')


def signindata(request):
    s=request.GET['fn']
    t=request.GET['ln']
    u=request.GET['mail']
    v=request.GET['pw']

    obj=sdata(fnm=s,lnm=t,email=u,paswrd=v)
    obj.save()
    return redirect('/login')

def cartpass(request):   
    a=request.GET['id']
    b=request.GET['nm']
    c=request.GET['pr']
    d=request.GET['mg']

    obj=cartitem(pname=b,pprice=c,pimage=d)
    obj.save()

    obj2=cartitem.objects.all()
    return render(request,'cart.html',{'cart':obj2})


def deletcart(request):
    a=request.GET['id']

    obj=cartitem.objects.get(id=a)
    obj.delete()

    obj2=cartitem.objects.all()
    return render(request,'cart.html',{'cart':obj2})


def plus(request):
    a=request.GET['id']

    obj=cartitem.objects.get(id=a)

    obj.ptotal=int(obj.ptotal)+50
    obj.pquantity=int(obj.pquantity)+1

    obj.save()

    obj2=cartitem.objects.all()
    return render(request,'cart.html',{'cart':obj2})


def minus(request):
    a=request.GET['id']

    obj=cartitem.objects.get(id=a)

    if(obj.pquantity<1):
        obj.delete()
    else:

        obj.ptotal=int(obj.ptotal)-50
        obj.pquantity=int(obj.pquantity)-1
        obj.save()

    obj2=cartitem.objects.all()
    return render(request,'cart.html',{'cart':obj2})


def js(request):
    obj=list(sdata.objects.values())

    return JsonResponse(obj,safe=False)
