from django.shortcuts import render

# Create your views here.
from course.models import Course
from videos.forms import VideoForm
from videos.models import Video


def create(request, id):
    course = Course.objects.get(id = id)
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.course_id = id
            f.save()
    else:
        form = VideoForm(request.POST)
    return render(request, 'admin/video/create.html', {'course': course, 'form': form})


def read(request):
    videos = Video.objects.all()
    return render(request, 'admin/video/view.html', {'videos': videos})


