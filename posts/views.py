from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Contact,Post,PostForm,Category


# Create your views here.









def home(request):
    return HttpResponse("Home")

def index(request):
    form=PostForm()
    data=Post.objects.all()
    categories=Category.objects.all()
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/posts/index')
    return render(request,'posts/index.html',{'data':data,'form':form,'Categories':categories})



def edit(request):
    if request.method=="POST":
        contact=Contact()
        contact.name=request.GET['name']
        contact.email=request.GET['email']
        contact.issue=request.GET['issue']
        contact.save()
        return redirect('/posts/contact')



def contact(request):
    if request.GET.get('method')=='edit':
        contact=Contact.objects.filter(id=request.GET.get('contactid')).get()
        print(contact.email)
        return render(request,'posts/edit.html',{'contact':contact})

    if request.GET.get('method')=='delete':
        contact=Contact.objects.filter(id=request.GET.get('contactid'))
        contact.delete()
        #return redirect("/posts/contact/")
    contacts=Contact.objects.all()
    print(contacts)
    res=render(request,'posts/contactus.html',{'contacts':contacts})
    return res