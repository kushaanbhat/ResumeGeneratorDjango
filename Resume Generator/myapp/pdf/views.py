from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io
# Create your views here.
def home(request):
    return render(request,"home.html")
def form(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        about=request.POST.get("about","")
        addline1=request.POST.get("addline1","")
        addline2=request.POST.get("addline2","")
        phone=request.POST.get("phone","")
        email=request.POST.get("email","")
        com1=request.POST.get("com1","")
        loc1=request.POST.get("loc1","")
        job1=request.POST.get("job1","")
        des1=request.POST.get("des1","")
        com2=request.POST.get("com2","")
        loc2=request.POST.get("loc2","")
        job2=request.POST.get("job2","")
        des2=request.POST.get("des2","")
        college=request.POST.get("college","")
        sloc1=request.POST.get("sloc1","")
        degree=request.POST.get("degree","")
        branch=request.POST.get("branch","")
        sdes1=request.POST.get("sdes1","")
        school1=request.POST.get("school1","")
        sloc2=request.POST.get("sloc2","")
        sdes2=request.POST.get("sdes2","")
        school2=request.POST.get("school2","")
        sloc3=request.POST.get("sloc3","")
        sdes3=request.POST.get("sdes3","")
        skill1=request.POST.get("skill1","")
        skill2=request.POST.get("skill2","")
        skill3=request.POST.get("skill3","")
        skill4=request.POST.get("skill4","")
        project1=request.POST.get("project1","")
        project2=request.POST.get("project2","")
        project3=request.POST.get("project3","")
        project4=request.POST.get("project4","")
        profile=Profile(name=name,about=about,addline1=addline1,addline2=addline2,phone=phone,email=email,com1=com1,loc1=loc1,job1=job1,des1=des1,com2=com2,loc2=loc2,job2=job2,des2=des2,college=college,sloc1=sloc1,degree=degree,branch=branch,sdes1=sdes1,school1=school1,sloc2=sloc2,sdes2=sdes2,school2=school2,sloc3=sloc3,sdes3=sdes3,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,project1=project1,project2=project2,project3=project3,project4=project4)
        profile.save()
    return render(request,"form.html")

def resume(request,id):
    user_profile=Profile.objects.get(pk=id)
    template=loader.get_template("resume.html")
    html=template.render()
    html=template.render({'user_profile':user_profile})
    options={
        'encoding':'UTF-8'
    }
    pdf=pdfkit.from_string(html,False,options)
    response= HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachments'
    return response
    # return render(request,"resume.html",{'user_profile':user_profile})

def list(request):
    profile=Profile.objects.all()
    return render(request,"list.html",{'profile':profile})