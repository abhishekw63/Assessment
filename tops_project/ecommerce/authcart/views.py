from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from .utils import TokenGenerator,generate_token

# from django.utils.encoding import force_bytes,force_text
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.generic import View

# from django.utils.http import DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode

from django.contrib.auth import authenticate,login,logout
def signup(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            # return HttpResponse('incorrect pwd')
            messages.warning(request,'passwordd is not matching')
            return render(request,'signup.html')
        try:
            if User.objects.get(username=email):
                messages.info(request,'Email is aoccupied')
                return render(request,'signup.html')
        except Exception as identifier:
            pass       
        user=User.objects.create_user(email,email,password)
        user.is_active=False
        user.save() 
        email_subject="Activate your account."
        message=render_to_string('activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid': urlsafe_base64_encode(str(user.pk).encode('utf-8')),
            'token':generate_token.make_token(user)
        })
        
        email_message=EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
        email_message.send()
        messages.success(request,'Activate your account by clicking the link in gmail')
        return redirect(reverse('handlelogin'))
    return render(request,'signup.html')

class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid = str(urlsafe_base64_decode(uidb64), 'utf-8')
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"Account Activated Successfully")
            return redirect('/auth/login')
        return render(request,'activatefail.html')
    
def handlelogin(request):
    if request.method=="POST":
        # print(request.POST) 
        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')

        else:
            messages.error(request,"Invalid Credentials")
            return redirect(reverse('handlelogin'))

    return render(request,'login.html') 

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/auth/login')