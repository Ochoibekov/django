from django import forms
from .models import Course, Homework


class CourseForms(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_title','content', 'id')


class HomeworkForms(forms.ModelForm):
    course_id = forms.ModelChoiceField(queryset=Course.objects.all())
    class Meta:
        model = Homework
        fields = ('course_title', 'content', 'course_id')