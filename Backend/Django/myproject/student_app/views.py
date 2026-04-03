from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentRegistrationForm
from .models import Student

# Django ORM - Object Relational Mapping

# Create your views here.
def student_list(request):
    # To fetch all data from the table or listing all data
    # Using objects.all() - ORM method

    # students object contains all data fetched from the table
    students = Student.objects.all()
    # students object is then passed to the respective template file or HTML file
    return render(request, "student_app/index.html", {'students': students})

def student_form(request):
    # ORM Method used: is_valid() & save()

    # If condition handles the insertion part
    if request.method == 'POST':
        # If the form is submitted through post method then this block will run to save the data in db
        # Request contains the data sent by the user in the form
        form = StudentRegistrationForm(request.POST)
        # First check the data, if it properly sent then store it or give the validation or error message
        if form.is_valid():
            form.save()
            # We should use named route for the redirection as that of the anchor tags
            return redirect('list_of_students')
    # Else condition handles to show the empty form
    else:
        form = StudentRegistrationForm()
    return render(request, "student_app/form.html", {'form': form})

def student_info(request, pk):
    # ORM Method used: get_object_or_404() to fetch single data w.r.t the primary key

    # The fetched data is stored in the student object which will be passed to html file
    student = get_object_or_404(Student, pk=pk)
    return render(request, "student_app/info.html", {'student': student})

# Difference b/w edit & update?
# Edit - Show Old data
# Update - Change Old data with New data
def edit_student(request, pk):
    # ORM Method used: is_vald(), get_object_or_404(), save()
    # It is combination of View & Insert
    
    # To fetch old data from DB
    student = get_object_or_404(Student, pk=pk)
    # To save the updated data
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_of_students')
    # To show the old data in the form
    else:
        # We will get the old data prefilled by using "instance=student" in the form
        form = StudentRegistrationForm(instance=student)
    return render(request, "student_app/form.html", {'form': form})

def delete_student(request, pk):
    # ORM Method used: delete(), get_object_or_404()
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('list_of_students')
    return render(request, "student_app/delete.html", {'student': student})