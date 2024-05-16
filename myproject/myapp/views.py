
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .crud_functions import create_student
from .forms import StudentForm
import pandas as pd
from django.core.files.storage import FileSystemStorage
import os



# def index(request):
#     return render(request, 'myapp/index.html')

# def some_function(request):
#     # Perform backend logic here
#     context = {'data': 'Hello, world!'}
#     return render(request, 'myapp/some_template.html', context)


def button(request):
   print('hello')

def loginUpdated_view(request):
    return render(request, 'myapp/loginUpdated.html')

def database_view(request):
    return render(request, 'myapp/database.html')

def scanproceed_view(request):
    return render(request, 'myapp/scanproceed.html')

def scansuccessful_view(request):
    return render(request, 'myapp/scansuccessful.html')

def scanunsuccessful_view(request):
    return render(request, 'myapp/scanunsuccessful.html')

def createstudent_view(request):
    return render(request, 'myapp/createstudent.html')



def createstudent_view(request):
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
            
            return redirect('studentlist')  # Redirect to the student list view

    else:
        form = StudentForm()
    return render(request, 'myapp/createstudent.html', {'form': form})

# def student_list_view(request):
#     updated_excel_path = os.path.join(settings.BASE_DIR, 'myapp', 'student_data_updated.xlsx')  # Use absolute path
#     df = pd.read_excel(updated_excel_path)  # Load the updated dataframe
#     students = df.to_dict(orient='records')
#     return render(request, 'myapp/studentlist.html', {'students': students})

def student_list_view(request, filename=None):
    if filename:
        fs = FileSystemStorage()
        file_path = fs.path(filename)

        try:
            # Load the dataframe from the uploaded Excel file
            df = pd.read_excel(file_path)
            students = df.to_dict(orient='records')
        except Exception as e:
            print(f"Error reading file: {e}")
            students = []
    else:
        students = []

    return render(request, 'myapp/studentlist.html', {'students': students})

def upload_excel_view(request):
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']
        fs = FileSystemStorage()
        filename = fs.save(excel_file.name, excel_file)
        file_path = fs.path(filename)

        try:
            # Process the uploaded Excel file
            df = pd.read_excel(file_path)
            students = df.to_dict(orient='records')

            # Optional: Save the updated Excel file back to storage
            updated_excel_path = os.path.join(fs.location, 'updated_' + filename)
            df.to_excel(updated_excel_path, index=False)

            # Redirect to the student list view with the filename as a parameter
            return redirect('student_list', filename=filename)
        except Exception as e:
            print(f"Error processing file: {e}")
            return render(request, 'myapp/upload_excel.html', {
                'error': 'There was an error processing the file. Please ensure it is a valid Excel file.'
            })

    return render(request, 'myapp/upload_excel.html')