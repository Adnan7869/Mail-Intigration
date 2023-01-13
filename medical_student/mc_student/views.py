from django.shortcuts import render,redirect,HttpResponse
from mc_student.models import Medical_Civil
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage

# Create your views here.

def home(request):
    return render(request,'index.html')


def medical(request):
    if request.method == 'POST':
        name=request.POST['name']
        collegename=request.POST['collegename']
        contact=request.POST['contact']
        batch=request.POST['batch']
        mail=request.POST['email']
        
        obj=Medical_Civil(name=name,college_name=collegename,cotact=contact,batch=batch,mail=mail)
        obj.save()
        return redirect('home')
    
    
def showmedical(request):
    show=Medical_Civil.objects.filter(batch ='Medical')
    context={'show':show}
    return render(request,'medical.html',context)


def showengineering(reqeust):
    shows=Medical_Civil.objects.filter(batch='Civil')
    context={'shows':shows}
    return render(reqeust,'civil.html',context)

def sendmail(request,id):
    s=Medical_Civil.objects.get(id=id)
    if request.method == 'POST':
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        email_form=settings.EMAIL_HOST_USER
        # var=s.mail.split()
        # print(">>>>>>>>>>>>",var)
        recipient_list=[s.mail,]
        # recipient_list=var
        # print('>>>>>>>>>>>>>',recipient_list)
        
        # recipient_list=['jc.junaid.chaudhary@gmail.com','bilalkhan965323@gmail.com','pasif387@gmail.com','himaliyasuraj@gmail.com','shaikhsaud8286@gmail.com','shaikhminhaj8850@gmail.com','khansarfraz5346@gmail.com','mumbaicodingclub@gmail.com','er.kmk123@gmail.com','shaikhsaud5539@gmail.com']
        send_mail(subject,message,email_form,recipient_list)
        return redirect('home')
    
    
    
def multimail(request):
    subject = request.POST['subject']
    print(">>>>>>>>>>>>>",subject)
    message = request.POST['message']
    print(">>>>>>>>>>>>>>>>>>",message)
    selected_emails = request.POST['selected-emails']
    email_list=selected_emails.split(',')
    print(">>>>>>>>>>>>>>>>>>>",selected_emails)
    email =EmailMessage(subject, message, to=email_list)
    email.send()
    return redirect('home')