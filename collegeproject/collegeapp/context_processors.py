from . models import Department,Course

def menu_dept(request):
    dept = Department.objects.all()
    return dict(dept=dept)

def menu_course(request):
    course = Course.objects.all()
    return dict(course=course)