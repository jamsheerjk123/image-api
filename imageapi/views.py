from django.shortcuts import render,HttpResponse
from django.template import RequestContext, Template, Context
from django.conf import settings
from account.models import Photo
from django.contrib.staticfiles.urls import static

# Create your views here.
def home(request):
    return render (request, 'index.html')


def all_images(request):
    images=Photo.objects.all()
    context={'images':images}
    return render (request, 'allimages.html',context)



def api_service(request,id):
    images=Photo.objects.get(id=id)
    k=images.picture.url
    print(k)
    
    return HttpResponse(f' <img src=" { k }" alt="hi" width=200px height=200px > ')