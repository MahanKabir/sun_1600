
from django import forms

from course.models import Course


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'type', 'price', 'image']