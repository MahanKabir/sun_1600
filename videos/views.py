from django.shortcuts import render

# Create your views here.
from videos.forms import VideoForm


def craete(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = VideoForm(request.POST)
    return render(request, 'admin/video/create.html', {'form': form})