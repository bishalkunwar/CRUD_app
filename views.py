from django.shortcuts import render, HttpResponsePermanentRedirect
from .forms import studentsRegistration
from .models import user

# Create your views here.
#Add and retrive/show method
def add_show(request):
    if request.method == 'POST':
        fm=studentsRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=user(name=nm,email=em,password=pw)
            reg.save()
            fm=studentsRegistration()

    else:
        fm=studentsRegistration()
    stud = user.objects.all()

    return render(request, 'enroll/addshow.html',{'form':fm,'stu': stud}) 

#Delete method:

def delete_data(request,id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponsePermanentRedirect('/')


#Update method:
def update_data(request,id):
    if request.method =='POST':
        pi = user.objects.get(pk=id)
        fm=studentsRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = user.objects.get(pk=id)
        fm=studentsRegistration(instance=pi)

    return render(request, 'enroll/updatestudents.html', {'form':fm})
    

