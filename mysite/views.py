from django.shortcuts import render,HttpResponse,redirect
from .models import Signup,Notes
from .forms import SignupForm, NotesForm
from django.contrib.auth import authenticate,logout
from django.core.mail import send_mail
from MyWebSite import settings
from django.contrib import messages




# Create your views here.

def index(request):
    if request.method=='POST':
        myfrm=SignupForm()
        if request.POST.get('submit')=='signup':
            myfrm=SignupForm(request.POST)
            if myfrm.is_valid():
                myfrm.save()

                
                subject = "Greetings"
                msg = "Congratulations! Now you are a member of DjangoSite."
                to = ["rudreshpatel93@gmail.com", "pranavparmar234@gmail.com", "kishanpatel4713@gmail.com"]
                res = send_mail(subject, msg, settings.EMAIL_HOST_USER, to)

                if(res == 1):
                    print("Mail Send Success!")
                    messages.success(request,'Registraion Done! Please check your registerd email.')
                    return redirect('notes')
                else:
                    print("Sending Faild!")
                    messages.error(request,'Somthing went wrong....Please try after some time!')
                    return redirect('/')
                
            else:
                return redirect('index')

        elif request.POST.get('submit')=='signin':
            
            email=request.POST['email']
            password=request.POST['password']

            uid=Signup.objects.get(email=email)
            print("Login ID:",uid.id)

            user=Signup.objects.filter(email=email,password=password)
            #user=authenticate(username=username,password=password)

            if user:
                    request.session['email']=email
                    request.session['uid']=uid.id
                    
                    messages.success(request,'Yooohooo! Successfully Logged in')
                    return redirect('notes')
            else:
                messages.error('Oops! Login Faild, Please try again.')
                return redirect('index')
    else:
        myfrm=SignupForm()
    return render(request,'index.html',{'myfrm':myfrm})



def notes(request):
    user=request.session.get('email')
    print("Function calling................")
    if request.method=='POST':
        
        mynotes=NotesForm(request.POST,request.FILES)
        if mynotes.is_valid():
            mynotes.save()
            print('Notes Upload Successfully!')
        else:
            print(mynotes.errors)
           
    else:
        mynotes=NotesForm()
        
    return render(request,'notes.html',{'mynotes':mynotes,'user':user})

def user_logout(request):
    logout(request)
    return redirect('index')

def updateprofile(request):
    id=request.session.get('uid')
    if request.method=='POST':
        stfrm=SignupForm(request.POST)
        print(stfrm)
        id=Signup.objects.get(id=id)
        if stfrm.is_valid():
            stfrm=SignupForm(request.POST, instance=id)
            stfrm.save()
    else:
        stfrm=SignupForm()
    return render(request,'updateprofile.html',{'stfrm':stfrm,'user':Signup.objects.get(id=id)})


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')