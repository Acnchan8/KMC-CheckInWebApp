from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .crud_functions import create_student
from .forms import StudentForm
import pandas as pd
import os

# def index(request):
#     return render(request, 'myapp/index.html')

# def some_function(request):
#     # Perform backend logic here
#     context = {'data': 'Hello, world!'}
#     return render(request, 'myapp/some_template.html', context)


def login_view(request):
    return render(request, 'myapp/login.html')

def database_view(request):
    return render(request, 'myapp/database.html')


def create_student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            excel_path = os.path.join(settings.BASE_DIR, 'myapp', 'student_data.xlsx')  # Use absolute path
            df = pd.read_excel(excel_path)  # Load your dataframe
            barcode = form.cleaned_data['barcode']
            id = form.cleaned_data['id']
            email = form.cleaned_data['email']
            student_class = form.cleaned_data['student_class']
            instructor = form.cleaned_data['instructor']
            name = form.cleaned_data['name']
            role = form.cleaned_data['role']
            department = form.cleaned_data['department']
            institution = form.cleaned_data['institution']
            service = form.cleaned_data['service']
            caseName = form.cleaned_data['caseName']
            
            updated_df = create_student(df, barcode, id, email, student_class, instructor, name, role, department, institution, service, caseName)
            updated_excel_path = os.path.join(settings.BASE_DIR, 'myapp', 'student_data_updated.xlsx')  # Use absolute path
            updated_df.to_excel(updated_excel_path, index=False)  # Save the updated dataframe
            
            return redirect('student_list')  # Redirect to the student list view

    else:
        form = StudentForm()
    return render(request, 'myapp/create_student.html', {'form': form})

def student_list_view(request):
    updated_excel_path = os.path.join(settings.BASE_DIR, 'myapp', 'student_data_updated.xlsx')  # Use absolute path
    df = pd.read_excel(updated_excel_path)  # Load the updated dataframe
    students = df.to_dict(orient='records')
    return render(request, 'myapp/student_list.html', {'students': students})