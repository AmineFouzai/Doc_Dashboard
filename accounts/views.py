from django.shortcuts import (render,redirect)
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.forms import (AuthenticationForm,UserCreationForm,PasswordResetForm,PasswordChangeForm)
from django.contrib.auth.models import User
from django.contrib.auth import (login,logout,update_session_auth_hash)
from django.core.mail import EmailMessage
from django.utils.http import (urlsafe_base64_encode,urlsafe_base64_decode)
from django.template.loader import render_to_string
from django.utils.encoding import (force_bytes,force_text)
from .token import Account_Vlidation_Token

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=("username","email","password1","password2")

class PasswordFormRest(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        del self.fields['old_password']
    class Meta:
        model=User
        fields=("new_password1","new_password2")

def Login_Request_Handler(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('index',permanent=True)
        else:
            form=AuthenticationForm()
            context={"form":form,"error":True}
            return render(request,'accounts/login.djt',context=context)
    else:
        form=AuthenticationForm()
        context={"form":form}
        return render(request,'accounts/login.djt',context=context)    



def Signup_Request_Handler(request):
    
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
                user=form.save(commit=False)
                user.is_active=False
                user.save()
                current_site=get_current_site(request)
                subject="Aactivate your Account !"
                body=render_to_string('accounts/activate.djt',{
                    'user':user,
                    'domain':current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':Account_Vlidation_Token.make_token(user)
                })
                mail_to=EmailMessage(subject=subject,body=body,to=[form.cleaned_data.get('email')])
                mail_to.send()
                return render(request,"accounts/check.djt",context={"type":False})            
        else:
            context={'form':form}
            return render(request,'accounts/signup.djt',context=context)
    else:
        form=SignupForm()
        context={'form':form}
        return render(request,'accounts/signup.djt',context=context)
   



def Rest_Password_Request_Handler(request):
        
        if request.method=="POST":
            form=PasswordResetForm(request.POST)
            if form.is_valid():
                try:
                    user=User.objects.get(email=form.cleaned_data.get('email'))
                    current_site=get_current_site(request)
                    subject="Reset your Password Account !"
                    body=render_to_string('accounts/resetpass.djt',{
                        'user':user,
                        'domain':current_site.domain,
                        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                        'token':Account_Vlidation_Token.make_token(user)
                        })
                    mail_to=EmailMessage(subject=subject,body=body,to=[form.cleaned_data.get('email')])
                    mail_to.send()
                    return render(request,'accounts/check.djt',context={"type":True})
                except Exception as e:
                     form=PasswordResetForm()
                     context={"form":form,'valid':False}
                     return render(request,'accounts/reset.djt',context=context)
            else:
                form=PasswordResetForm()
                context={"form":form,'valid':False}
                return render(request,'accounts/reset.djt',context=context)
        else:
            form=PasswordResetForm()
            context={"form":form,'valid':True}
            return render(request,'accounts/reset.djt',context=context)


def Valid_Reset_Password_Hequest_Handler(request,uid,token):
    try:
        uid=force_text(urlsafe_base64_decode(uid))
        user=User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist) as e:
        user=None
    if user is not None and Account_Vlidation_Token.check_token(user,token):
        if request.method=="POST":
            form=PasswordFormRest(data=request.POST,user=user)
            if form.is_valid():
                form.save(commit=True)
                update_session_auth_hash(request,user)
                return redirect('login',permanent=False)
            else:
                url=request.get_full_path().split('/')
                form=PasswordFormRest(user)
                context={'form':form,'uid':url[-2],'token':url[-1],"error":True}
                return render(request,'accounts/changepass.djt',context=context)
        else:
            url=request.get_full_path().split('/')
            form=PasswordFormRest(user)
            context={'form':form,'uid':url[-2],'token':url[-1]}
            return render(request,'accounts/changepass.djt',context=context)

    else:
       return render(request,'accounts/valid.djt')
   



def Valid_Email_Request_Handler(request,uid,token):
    try:
        uid=force_text(urlsafe_base64_decode(uid))
        user=User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None
    if user is not None and Account_Vlidation_Token.check_token(user,token):
        user.is_active=True
        user.save()
        login(request,user)
        return redirect('index',permanent=True)
    else:
        return render(request,'accounts/valid.djt')
   

def Logout_Request_Hanlder(request):
    if request.method=="POST":
        logout(request)
        return redirect('login')
    else:
        logout(request)
        return redirect('login')
