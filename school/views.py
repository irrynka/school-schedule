from django.shortcuts import render,redirect
from .models import Subject, Teacher, Class, Student

# Create your views here.
def add_items(request):
    if 'subject_name' in request.POST:
        Subject.objects.create(name=request.POST['subject_name'])
        return redirect('add_items')
    
    if 'class_name' in request.POST:
        Class.objects.create(name=request.POST['class_name'])
        return redirect('add_items')
    
    if 'teacher_name' in request.POST and 'teacher_subject' in request.POST:
        subject = Subject.objects.get(id=request.POST['teacher_subject'])
        Teacher.objects.create(name=request.POST['teacher_name'], subject=subject)
        return redirect('add_items')
    
    if 'student_name' in request.POST and 'student_class' in request.POST:
        class_group = Class.objects.get(id=request.POST['student_class'])
        Student.objects.create(name=request.POST['student_name'], class_group=class_group)
        return redirect('add_items')
    
    subjects = Subject.objects.all()
    classes = Class.objects.all()

    return render(request, 'add_items.html', {'subjects': subjects, 'classes': classes})