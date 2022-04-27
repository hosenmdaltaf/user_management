from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import  User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import UserRegisterForm

# Create your views here.
@login_required(login_url ='/')
def homepage(request):
    return HttpResponse('Hi ------------------------ this is home page ---------------')



def logout(request):
    return HttpResponse('Hi logoutpage ---------------')

def password_reset(request):
    return HttpResponse('Hi passwordpage ---------------')

def register_edit(request):
    return HttpResponse('Hi register_editpage ---------------')

# username, first_name, last_name, email, password = kwargs['username'], kwargs['first_name'], kwargs['last_name'], kwargs['email'], kwargs['password1']
#         user = User(username=username, email=email, first_name=first_name, last_name=last_name)
#         user.set_password(password)
#         user.save()



def registerview(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # username_exists = User.objects.filter(username=username)
        # if username_exists.exists():
        #     messages.warning(request,  'Please select another username this name already exist')
        #     return redirect('account:registerpage')

        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect('account:registerpage')

        if password1 != password2 :
            messages.warning(request,  'Your password is not same!')
            return redirect('account:registerpage')
        email_exists = User.objects.filter(email=email)
        if email_exists.exists():
            messages.warning(request,  'Please select another email this email already in use')
            return redirect('account:registerpage')       
        else:

            # new_user = User.objects.create(username=username, email=email, password=password)
            # new_user = form.save(commit=False)
            # ...
            # new_user.save()

            newUser=User.objects.create_user(username=username,email=email,password=password1)
            # b=newUser.set_password(password1)
            newUser.save()
            messages.success(request,  'Your account has been successfully created')
            return redirect('account:homepage')

        # username = newUser.cleaned_data.get('username')
        # raw_password = newUser.cleaned_data.get('password1')
        # user = authenticate(username=username, password=raw_password)
        # login(request, user)
        # return redirect('homepage')
    return render(request,'account/register.html') 

def loginview(request):
    # user =request.user
    # if user.is_authenticated:
    #     return redirect("homepage")
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account:homepage')
    return render(request,'account/login.html') 


def logout_view(request):
    logout(request)



