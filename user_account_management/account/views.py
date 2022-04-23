
from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import  User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import UserRegisterForm

# Create your views here.
@login_required(login_url ='/')
def homepage(request):
    return HttpResponse('This is homepage friends ---------------')



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



# def register(request):
#     if request.POST.get("form_type") == 'formOne':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         if password1 != password2 :
#             messages.warning(request,  'Your password is not currect!')
#         if username.exist()
#             messages.warning(request,  'Please select another username this name already exist')
#         if email.exits()
#             messages.warning(request,  'Please select another email this email already in use')
#         else:
#             newUser=User.objects.create_user(username=username,email=email,password1=password1,password2=password2)
#             print(newUser)
#             b=newUser.save()
#             print(b)
#             messages.success(request,  'Your account has been successfully created')

#         # username = newUser.cleaned_data.get('username')
#         # raw_password = newUser.cleaned_data.get('password1')
#         # user = authenticate(username=username, password=raw_password)
#         # login(request, user)
#         # return redirect('homepage')
#     return render(request,'account/homepage.html') 
        

def loginview(request):
    # user =request.user
    # if user.is_authenticated:
    #     return redirect("homepage")
    if request.POST.get("form_type") == 'formTwo': 

        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
    return render(request,'account/homepage.html') 


def logout_view(request):
    logout(request)



