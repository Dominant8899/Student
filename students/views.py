from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def student_list(request):
    query = request.GET.get('q')

    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()

    context = {
        'students': students,
        'query': query,
        'total_students': Student.objects.count()
    }
    return render(request, 'student_list.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def edit_student(request, student_id=None):
    if student_id is None:
        students = Student.objects.all()
        return render(request, 'edit_student.html', {'students': students, 'student': None})

    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'edit_student.html', {'form': form, 'student': student})

@login_required
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('student_list')

@login_required
def home_view(request):
    context = {
        'total_students': Student.objects.count()
    }
    return render(request, 'home.html', context)

@login_required
def contact_view(request):
    return render(request, 'contact.html')