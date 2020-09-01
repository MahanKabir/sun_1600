from django.shortcuts import render, redirect

# Create your views here.
from course.forms import CourseForm
from course.models import Course


def create(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CourseForm()

    return render(request, 'admin/course/create.html')

def read(request):
    courses = Course.objects.all()
    return render(request, 'admin/course/view.html', {'courses': courses})

def update(request, id):
    pass

def delete(request, id):
    course = Course.objects.get(id = id)
    course.delete()
    return redirect('course.view')