from django.shortcuts import render

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

    return render(request, 'admin/course/create.html', {'form': form})

def read(request):
    courses = Course.objects.all()
    return render(request, 'admin/course/view.html', {'courses': courses})

def update(request):
    pass

def delete(request):
    pass