from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import *


# Create your views here.
def create_topic(request):
    if request.method=="POST":
        topic=request.POST.get("topic")
        t=Topic.objects.get_or_create(topic_name=topic)
        if t[1]==True:
            t[0].save()
            return HttpResponse("<h3>Topic Added Successfully</h3>")
        else:
            return HttpResponse("<h3>Topic Is Already Exist In Table</h3>")
    return render(request,"create_topic.html")

def create_webpage(request):
    if request.method=="POST":
        topic=request.POST.get('topic')
        name=request.POST.get('name')
        url=request.POST.get("url")
        t=Topic.objects.get_or_create(topic_name=topic)[0]
        w=Webpage.objects.get_or_create(topic=t,name=name,url=url)[0]
        w.save()
        return HttpResponse("<h3>Webpage Added Successfully</h3>")
    topics=Topic.objects.all()
    return render(request,"create_webpage.html",context={'topics':topics})

def create_accessdetails(request):
    if request.method=="POST":
        webpage=request.POST.get('webpage')
        datetime=request.POST.get('datetime')
        w=Webpage.objects.get_or_create(name=webpage)[0]
        a=AccessDetails.objects.get_or_create(webpage=w,datetime=datetime)[0]
        a.save()
        return HttpResponse("<h3>Webpage Added Successfully</h3>")
    webpages=Webpage.objects.all()
    return render(request,"create_accessdetails.html",context={'webpages':webpages})

def display_topics(request):
    topics=Topic.objects.all()
    return render(request,"display_topic.html",\
        context={'topics':topics})

def display_webpages(request):
    webpages=Webpage.objects.all()
    return render(request,"display_webpage.html",\
        context={'webpages':webpages})

#accessing the specific data present in the database by passing the pk
#in the url
def display_topic(request,id):
    topics=Topic.objects.filter(id=id)
    return render(request,"display_topic.html",\
        context={'topics':topics})

def display_webpage(request,webid):
    webpages=Webpage.objects.filter(id=webid)
    return render(request,"display_webpage.html",\
        context={'webpages':webpages})

def display_accessdetails(request):
    accessdetail=AccessDetails.objects.all()
    return render(request,"display_accessdetails.html",\
        context={'accessdetail':accessdetail})

def display_accessdetails(request):
    accessdetail=AccessDetails.objects.all()
    return render(request,"display_accessdetails.html",\
        context={'accessdetail':accessdetail})

def display_accessdetails(request,aid):
    accessdetail=AccessDetails.objects.filter(id=aid)
    return render(request,"display_accessdetails.html",\
        context={'accessdetail':accessdetail})

def search_webpage(request):
    if request.GET.get('search'):
        id=request.GET['search']
        return redirect('display_webpage',webid=id)
    return render(request,'search_webpage.html')
    
def update_topic(request,id):
    if request.method=="POST":
        new_tname=request.POST.get("topic_name")
        t=Topic.objects.filter(id=id).update(topic_name=new_tname)
    t=Topic.objects.get(id=id)
    return render(request,"update_topic.html",{"topic":t})

def update_webpage(request,id):
    if request.method=="POST":
        topic=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        t=Topic.objects.get(topic_name=topic)
        w=Webpage.objects.filter(id=id).update(topic=t,name=name,url=url)
    t=Topic.objects.all()
    webpage=Webpage.objects.get(id=id)
    return render(request,"update_webpage.html",{"topics":t,'webpage':webpage})

def delete_topic(request,id):
    t=Topic.objects.filter(id=id)
    if t:
        t.delete()
        return HttpResponse("<h3>deletion is duccessful</h3>")
    return HttpResponse("<h3>Record not found</h3>")

def update_accessdetails(request,id):
    if request.method=="POST":
        webpage=request.POST['webpage']
        datetime=request.POST['datetime']
        w=Webpage.objects.get(webpage_name=webpages)
        a=AccessDetails.objects.filter(id=id).update(webpages=w,datetime=datetime)
    w=Webpage.objects.all()
    accessdetail=AccessDetails.objects.get(id=id)
    return render(request,"update_accessdetails.html",{"webpages":w,'accessdetail':accessdetail})

def delete_topic(request,id):
    t=Topic.objects.filter(id=id)
    if t:
        t.delete()
        return HttpResponse("<h3>deletion is successful</h3>")
    return HttpResponse("<h3>Record not found</h3>")

def display_image(request,id):
    profile=ProfilePic.objects.get(id=id)
    return render(request,"display_image.html",{'profile':profile})

from myapp.forms import *
def topic_modelform(request):
    if request.method=="POST":
        form=TopicForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,'model_form.html',{'form':form})
    form=TopicForm()
    return render(request,'model_form.html',{'form':form})
def webform(request):
    if request.method=="POST":
        form=WebpageForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,'model_form.html',{'form':form})
    form=WebpageForm()
    return render(request,'model_form.html',{'form':form})
def accessdetails(request):
    if request.method=="POST":
        form=AccessDetailsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,'model_form.html',{'form':form})
    form=AccessDetailsForm()
    return render(request,'model_form.html',{'form':form})


def create_user(request):
    if request.method=="POST":
        user=UserModelForm(request.POST)
        if user.is_valid():
            password=user.cleaned_data['password']
            user=user.save(commit=False)
            user.set_password(password)
            user.save()
    form=UserModelForm()
    return render(request,"model_form.html",{'form':form})










