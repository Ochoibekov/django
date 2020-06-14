from django.shortcuts import render
from django import forms
# Create your views here.
from lesson.forms import CourseForms, HomeworkForms
from lesson.models import Course, Homework


def new_lesson(request):
    form = CourseForms(request.POST)
    if form.is_valid():
        me = form.save(commit=False)
        me.save()
    return render(request,'lesson/new_lesson.html',{'form': form})


def new_homework(request):
    form = HomeworkForms(request.POST)
    if form.is_valid():
        my_friend = form.save(commit=False)
        my_friend.save()
    return render(request, 'lesson/new_homework.html', {'form': form})

def homepage(request):
    lessons = Course.objects.all()
    return render(request, 'lesson/homepage.html', {'lessons': lessons, 'homeworks': homeworks})

def homeworks(request):
    homeworks = Homework.objects.all()
    return render(request, 'lesson/homeworks.html', {'homeworks': homeworks})

def homework_show_page(request, course_id):
    Course_id = format(course_id)
    homework_show = Homework.objects.all().filter(course_id=Course_id)
    print(homework_show.count())
    return render(request, 'lesson/homework_show_page.html', {'homework_show_page': homework_show})