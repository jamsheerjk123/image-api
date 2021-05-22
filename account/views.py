from django.shortcuts import render,HttpResponse,redirect
from .forms import RegisterForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import authenticate,login,logout
from .models import ApiKey
# Create your views here.
def signup(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            
            key=default_token_generator.make_token(user)
            api=ApiKey.objects.create (user=user,key=key)
            api.save()
            return redirect('accounts:signin')
        return render (request,'register.html',{'form':form})    

    form=RegisterForm()
    return render (request,'register.html',{'form': form})    

def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        print("hello")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request, user)
            return HttpResponse("Succesfully Logged in")
        return HttpResponse('incorect username or password')    
     
    return render (request,'login.html')

