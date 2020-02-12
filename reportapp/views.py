from django.shortcuts import render,redirect,get_object_or_404
# from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib.auth import login,authenticate,logout
from .forms import regform,userform,login_form,upform,userupform,topicform,subtopicform,reportform,contactform
from .models import profile,subtopic1,topic1
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.models import User
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template.loader import render_to_string

# Create your views here.
class homeview(TemplateView):
    template_name = 'home.html'
    

class registerform(View):
    def get(self,request,*args, **kwargs):
        model = profile
        reg_form = regform
        user_form = userform
        return render(request,'register.html',{'reg_form':reg_form,'user_form':user_form})
    
    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            reg_form = regform(request.POST,request.FILES)
            user_form = userform(request.POST)
            if reg_form.is_valid() and user_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                
                reg = reg_form.save(commit=False)
                reg.user = user
                reg.email = user.email
                reg.up = False
                reg.save()
                return redirect('reportapp:login')
            else:
                print(user_form.errors,reg_form.errors)
                return HttpResponse('Fail')
        
class loginview(View):      
    def get(self,request):
        logform = login_form
        return render(request,'login.html',{'logform':logform})
    
    def post(self,request,*args, **kwargs):
        
        if request.method == 'POST':
            us = request.POST['username']
            pwd = request.POST['password']
            user = authenticate(username=us,password=pwd)
            if user:
                if user.is_active:
                    login(request,user)
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else: 
                        us = profile.objects.get(user=request.user)
                        field_object = profile._meta.get_field('up')
                        field_value = getattr(us, field_object.attname)
                        if field_value == False:
                            return redirect('reportapp:update')
                        else:
                            return redirect('reportapp:home')
                else:
                    return HttpResponse('Account not active')
            else:
                return HttpResponse('login failed')
        else:
            return redirect('reportapp:login')
    
class logoutview(View):
    
    def get(self,request):
        logout(request)
        return redirect('reportapp:home')
    
class updateview(View):
    
    def get(self,request,*args, **kwargs):
        user = User.objects.get(username=request.user)
        pid = profile.objects.get(user=user)
        uform = userupform(instance=user)
        updateform = upform(instance=pid)
        return render(request,'update.html',{'uform':uform,'updateform':updateform})
        
    def post(self,request,*args,**kwargs):
        up = False
        user = User.objects.get(username=request.user)
        pid = profile.objects.get(user=user)
        try:
            if request.method == 'POST':
                updateform = upform(request.POST,request.FILES,instance=pid)
                uform = userupform(data=request.POST,instance=user)
                
                if updateform.is_valid() and uform.is_valid():
                    a = uform.save(commit=False)
                    a.save()
                    
                    b  = updateform.save(commit=False)
                    b.user = a
                    b.email = a.email
                    b.up = True
                    b.save()
                    up = True
                    if up == False:
                        return redirect('reportapp:login')
                    else:
                        return redirect('reportapp:home')
        except:
            return HttpResponse('fail')
        # return render(request,'update.html')
        
class deleteview(View):
    def get(self,request,*args, **kwargs):
        pass
    
    def post(self,request,*args, **kwargs):
        user = User.objects.get(username=request.user)
        
        if request.method == 'POST':
            user.delete()
            return redirect('reportapp:home')
            
class topicview(View):
    @method_decorator(login_required(login_url='reportapp:login'))
    def get(self,request,*args, **kwargs):
        topic_form = topicform()
        subtopic_form = subtopicform()
        return render(request,'dailyrec.html',{'topic_form':topic_form,'subtopic_form':subtopic_form})
    
    def post(self,request,*args, **kwargs):
        topic_form = topicform(request.POST)
        # subtopic_form = subtopicform(request.POST)
        if request.method == 'POST':
            if topic_form.is_valid():
                topic = topic_form.save(commit=False)
                topic.user = request.user
                topic.save()
                return redirect('reportapp:topic')
            else:
                return HttpResponse('fail')
        else:
            return HttpResponse('nopost')
        
class subtopicview(View):
    @method_decorator(login_required(login_url='reportapp:login'))
    def get(self,request,*args, **kwargs):
        topic_form = topicform()
        subtopic_form = subtopicform()
        return render(request,'dailyrec.html',{'topic_form':topic_form,'subtopic_form':subtopic_form})
    
    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            subtopic_form  = subtopicform(request.POST)
            user = profile.objects.get(user = request.user)
            if subtopic_form.is_valid():
                subt = subtopic_form.save(commit=False)
                subt.user = request.user
                subt.save()
                return redirect('reportapp:subtopic')
            else:
                return HttpResponse('fail')
        else:
            return HttpResponse('nopost')

class reportview(View):
    def get(self,request):
        st = subtopic1.objects.all()
        st_filter = st.filter(user=request.user)
        return render(request,'report.html',{'st_filter':st_filter})
    
class uprecordview(View):
    def get(self,request,subtopicid,*args,**kwargs):
        rid = subtopic1.objects.get(id=subtopicid)
        subtopic_form = subtopicform(instance=rid)
        return render(request,'updatedailyrec.html',{'subtopic_form':subtopic_form})

    def post(self,request,subtopicid,*args,**kwargs):
        rid = subtopic1.objects.get(id=subtopicid)
        if request.method == 'POST':
            subtopic_form = subtopicform(request.POST,instance=rid)
            if subtopic_form.is_valid():
                subtopic_form.save()
                return redirect('reportapp:report')
            else:
                return HttpResponse('fail')

class deleterecview(View):
    def get(self,request,*args,**kwargs):
        pass
    
    def post(self,request,delsubtopicid,*args,**kwargs):
        did = subtopic1.objects.get(id=delsubtopicid)
        if request.method == 'POST':
            did.delete()
            return redirect('reportapp:report')
        else:
            return HttpResponse('fail')
        return HttpResponse("nopost")
            
class topicdisplayview(View):
    def get(self,request,*args, **kwargs):
        topic = topic1.objects.all()
        topic_filter = topic.filter(user=request.user)
        return render(request,'topiclist.html',{'topic_filter':topic_filter})

class uptopicview(View):
    def get(self,request,topicid,*args, **kwargs):
        tid = topic1.objects.get(pk=topicid)
        topic_form = topicform(instance=tid)
        return render(request,'uptopic.html',{'topic_form':topic_form})
    
    def post(self,request,topicid,*args, **kwargs):
        tid = topic1.objects.get(pk=topicid)
        if request.method=='POST':
            topic_form = topicform(request.POST,instance=tid)
            if topic_form.is_valid():
                topic_form.save()
                return redirect('reportapp:topicdisplay')
            

class deltopicview(View):
    def post(self,request,topicid,*args,**kwargs):
        tid = topic1.objects.get(pk=topicid)
        if request.method == 'POST':
            tid.delete()
            return redirect('reportapp:topicdisplay')
    
class generatereport(View):
    def get(self,request,*args,**kwargs):
        report_form=reportform()
        return render(request,'reportform.html',{'report_form':report_form})
    
    def post(self,request,*args, **kwargs):
        if request.method =='POST':
            sdate = request.POST['start_date']
            edate = request.POST['end_date']
            data = subtopic1.objects.filter(date__range=[sdate, edate])
            topi = topic1.objects.filter(date__range=[sdate,edate])
            tuser = topi.filter(user=request.user)
            duser = data.filter(user=request.user)
            p = profile.objects.filter(user = request.user)
            context = {'p':p,'sdate':sdate,'edate':edate,'duser':duser,'tuser':tuser}
            return render(request,'finalreport.html',context)
            
class contactus(View):
    def get(self,request,*args, **kwargs):
        contact_form = contactform
        return render(request,'contactus.html',{'contact_form':contact_form})
    
    def post(self,request,*args, **kwargs):
        i  = False
        if request.method == 'POST':
            contact_form = contactform
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            sub = request.POST['subject']
            msg = request.POST['message']
            
            msg_html = render_to_string('email.html', {'fname': fname,'lname': lname,'email': email,'sub': sub,'msg': msg})

            send_mail(sub,msg,
                settings.EMAIL_HOST_USER,
                ['darshan2297@zohomail.in'],
                html_message=msg_html,
            )
            
            i = True
            
            return render(request,'contactus.html',{'contact_form':contact_form,'i':i})


class aboutus(TemplateView):
    template_name = 'aboutus.html'
    