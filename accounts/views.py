from django.shortcuts import render , redirect
from django.contrib.auth import login ,authenticate , logout
# Create your views here.
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.


def login_view(request):
    
#    if request.user.authenticated:
#        return render(request,"accounts/already-logged.html",{})
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/')
    else:
        form=AuthenticationForm(request)
    context={'form':form}
    return render(request,"accounts/login.html",context=context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login/')
    return render(request,"accounts/logout.html",{})


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login/')
    return render(request,'accounts/register.html',{'form':form})
