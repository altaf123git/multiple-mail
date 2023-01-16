from django.shortcuts import render
from django.http import HttpResponse
from studentapp.models import Student
from django.core.mail import send_mail
from student import settings 
from django.conf import settings

# Create your views here.
def home(request):
    return render(request,'home.html')

def insert(request):
    if (request.method=='POST'):
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        field=request.POST['field']
        college=request.POST['college']
        city=request.POST['city']
        print(fname)
        if (len(fname)==0 or len(lname)==0 ):
            return HttpResponse("null value not allowed")
        
        student=Student(first_name=fname, last_name=lname, email=email, field=field, college=college, city=city)
        
        student.save()
    return render(request,'insert.html')

def medical(request):
    record= Student.objects.filter(field="medical")
    return render(request,'medical.html', {'record':record})

def engineer(request):
    record= Student.objects.filter(field="engineer")
    return render(request,'engineer.html', {'record':record})

# def mail(request):
#     if (request.method=='POST'):
#         #send_mail('this is subject','this is message body',['altaf.capg@gmail.com'], fail_silently=False) 
#         subject = "subject here"  
#         msg     = "Congratulations for your success"  
#         to      = "altaf.capg@gmail.com"  
#         res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
#         if(res == 1):  
#             msg = "Mail Sent Successfuly"  
#         else:  
#             msg = "Mail could not sent"  
#         return HttpResponse(msg)
#     return render(request,'mail.html')

def mail(request):
    multiple=[]
    if (request.method=='POST'):
        mail_list = request.POST.getlist('multiple')
        
        #send_mail('this is subject','this is message body',['altaf.capg@gmail.com'], fail_silently=False) 
        subject = request.POST['subject'] 
        msg     = request.POST['message'] 
        print(mail_list)
    
        #to      =multiple
        #to      = ["altaf.capg@gmail.com","2020.altaf.chaudhary@ves.ac.in"]
        res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, mail_list)  
        if(res == 1):  
            msg = "Mail Sent Successfuly"  
        else:  
            msg = "Mail could not sent"  
        return HttpResponse(msg)
    return render(request,'engineer.html')

def sendmail(request, id):
    record=Student.objects.get(id=id)
    if (request.method=='POST'):
        #send_mail('this is subject','this is message body',['altaf.capg@gmail.com'], fail_silently=False) 
        subject = request.POST['subject'] 
        msg     = request.POST['message']
        
        to      =record.email
        #to      = ["altaf.capg@gmail.com","2020.altaf.chaudhary@ves.ac.in"]
        res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
        if(res == 1):  
            msg = "Mail Sent Successfuly"  
        else:  
            msg = "Mail could not sent"  
        return HttpResponse(msg)
    return render(request,'mail.html', {"record":record})

