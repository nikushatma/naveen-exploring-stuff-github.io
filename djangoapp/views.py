from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from shop.models import Product
from shop.models import Contact
# from math import ceil

def HomePage(request):
    Addproducts = Product.objects.all()
    data ={
        'Addproducts':Addproducts,
        }

    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # params={'no_of_slides':nSlides,'range':range(nSlides),'product':products}
    return render(request,"shop.html",data)

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact=contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,"contact.html")

def tracker(request):
    return render(request,"tracker.html")

def search(request):
    return render(request,"search.html")

def productview(request,myid):
    product = Product.objects.filter(id=myid)
    data ={
        'product':product[0]
        }
    return render(request,"productview.html",data)

def checkout(request):
    return render(request,"checkout.html")




























# from .forms import UserForm


# def HomePage(request):
#     data = {
#         'title':'home page',
#         'bdata':'student',
#         'list':['PHP','JAVA','C++','PYTHON'],
#         'student_detail':[
#             {'name':'Naveen','phoneno':'8882970612'},
#             {'name':'Navneet','phoneno':'9999744239'}
#         ],
#         'number':[]
#     }
#     return render(request,"index.html",data)

# def aboutus(request):
#     if request.method=="GET":
#         data=request.GET.get('data')
#     return render(request,"thanku.html",{'data':data})

# def userform(request):
#     result=0
#     re=UserForm()
#     data ={'form':re}
#     try:
#         if request.method=="POST":
#             n1=int(request.POST.get('num1'))
#             n2=int(request.POST.get('num2'))
#             result=n1+n2
#             data={
#                 'form':re,
#                 'output':result
#             }
#             url="/aboutus/?output={}".format(result)

#             return HttpResponseRedirect(url)
#     except:
#         pass
#     return render(request,"userforms.html",data)

# def submitform(request):
#     result=0
#     # re=userform()
#     data ={}
#     try:
#         if request.method=="POST":
#             n1=int(request.POST.get('num1'))
#             n2=int(request.POST.get('num2'))
#             result=n1+n2
#             data={
#                 'n1':n1,
#                 'n2':n2,
#                 'output':result
#             }
#             url="/aboutus/?output={}".format(result)

#             return redirect(url)
#     except:
#         pass

# def calculator(request):
#     c=''
#     try:
#         if request.method=="POST":
#             n1=eval(request.POST.get('num1'))
#             n2=eval(request.POST.get('num2'))
#             opr=request.POST.get('opr')
#             if opr=="+":
#                 c=n1+n2
#             elif opr=="-":
#                 c=n1-n2
#             elif opr=="*":
#                 c=n1*n2
#             elif opr=="/":
#                 c=n1/n2
#     except:
#         c="Inavid operations......."
#     print(c)
#     return render(request,"calculator.html",{'c':c})

# def saveevenodd(request):
#     c=''
#     if request.method=="POST":
#         if request.POST.get('num1')=="":
#             return render(request,"evenodd.html",{'error':True})
#         n = eval(request.POST.get('num1'))
#         if n%2==0:
#             c="Even number"
#         else:
#             c="Odd number"

#     return render(request,"evenodd.html",{'c':c})

# def marksheet(request):
#     data={}
#     if request.method=="POST":
#         s1=eval(request.POST.get('num1'))
#         s2=eval(request.POST.get('num2'))
#         s3=eval(request.POST.get('num3'))
#         s4=eval(request.POST.get('num4'))
#         s5=eval(request.POST.get('num5'))
#         t=s1+s2+s3+s4+s5
#         p=(t/500)*100
#         if p>=80:
#             d="First div"
#         elif p>=70:
#             d="Second div"
#         elif p>=50:
#             d="Third div"
#         elif p>=33:
#             d="Pass"
#         else:
#             d="Fail"
#         data={
#             'total':t,
#             'percentage':p,
#             'div':d
#             }
    
#     return render(request,"marksheet.html",data)



