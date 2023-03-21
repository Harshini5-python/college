from django.http import HttpResponse
from django.shortcuts import render
from . models import Requirements,Department,Course
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "home.html")

def allcourse(request):
    return render(request,"allcourse.html")

def regform(request):
    dept = Department.objects.all()
    if request.method == "POST":
        name = request.POST.get('name', '')
        age = request.POST.get('age', '')
        dob = request.POST.get('dob', '')
        gender = request.POST.get('gender','')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        # deptt = request.POST('dept','')
        # coursee = request.POST('course','')
        purpose = request.POST.get('purpose', '')
        material = request.POST.getlist('checks[]','')

        task = Requirements(name=name, age=age, dob=dob, gender=gender, phone=phone, email=email, address=address, purpose=purpose, material=material)
        task.save()
        messages.success(request, "Form submitted successfully!")
        # return redirect('/')

    return render(request,"regform.html",{'dept':dept})



def get_course(request):
    # dept = Department.objects.all()
    # course = Course.objects.all()
    dept_id = request.GET['dept_id']
    get_dept = Department.objects.get(id=dept_id)
    course = Course.objects.filter(dept=get_dept)
    return render(request, 'get-course.html', locals())




