from multiprocessing import context
from django.shortcuts import render,redirect

from Emp_Manage_sys_app.forms import EmployeeForm
from Emp_Manage_sys_app.models import Employee
from django.db.models import Q

# Create your views here.
def index(request):
    templates_name='index.html'
    return render(request,templates_name)

def all_emp(request): 
    obj=Employee.objects.all()
    context={'obj':obj}
    templates_name='all_emp.html'
    return render(request,templates_name,context)

def add_emp(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('all_emp')
    form=EmployeeForm()
    context={'form':form}
    templates_name='add_emp.html'
    return render(request,templates_name,context)

def remove_emp(request):
    obj=Employee.objects.all()
    context={'obj':obj}
    template_name='remove_emp.html'
    return render(request,template_name,context)


def filter_emp(request):
    if 'q' in request.GET:
        q=request.GET['q']
        # data=Data.objects.filter(first_name__icontains=q)
        if q:
            multiple_q=Q(Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(phone__icontains=q))
            data=Employee.objects.filter(multiple_q)
    else:
        data=Employee.objects.all()
    context={
        'data':data
    }
    templates_name='filter_emp.html'
    return render(request,templates_name,context)




def delete(request,id):
    obj=Employee.objects.get(id=id)
    obj.delete()
    return redirect('all_emp')

def update_emp(request):
    obj=Employee.objects.all()
    templates_name='update_emp.html'
    context={'obj':obj}
    return render(request,templates_name,context)

def update(request,id):
    obj=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=obj)
        if form.is_valid:
            form.save()
            return redirect('all_emp')
    form=EmployeeForm(instance=obj)
    context={'form':form}
    templates_name='update_forms.html'
    return render(request,templates_name,context)