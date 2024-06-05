
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .crud_functions import create_student_database, update_student, get_student, delete_student
from .forms import CreateStudentForm, SearchForm, UpdateStudentForm, DeleteForm
import pandas as pd
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

def scanproceed_view(request):
    return render(request, 'myapp/scanproceed.html')

def scansuccessful_view(request):
    return render(request, 'myapp/scansuccessful.html')

def scanunsuccessful_view(request):
    return render(request, 'myapp/scanunsuccessful.html')

def database_view(request, dataset='default'):
    dataset_files = {
        'default': 'KMC_Student_Database.xlsx',
        'checkin': 'KMC_Master_Checkin.xlsx',
        'student': 'KMC_Student_Database.xlsx',
    }
    excel_file = dataset_files.get(dataset, 'KMC_Master_Checkin.xlsx')
    excel_path = os.path.join(settings.MEDIA_ROOT, excel_file)
    df = pd.read_excel(excel_path)

    query = request.GET.get('search')
    if query:
        df = df[df.apply(lambda row: row.astype(str).str.contains(query).any(), axis=1)]

    html_table = df.to_html(index=False, classes='dataframe')
    return render(request, 'myapp/database.html', {'data_html': html_table, 'dataset': dataset})

def createstudent_view(request):
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            excel_path = os.path.join(settings.BASE_DIR, 'media', 'KMC_Student_Database.xlsx')  # Use absolute path
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
            
            updated_df = create_student_database(df, barcode, id, email, student_class, instructor, name, role, department, institution, service, caseName)
            updated_excel_path = os.path.join(settings.BASE_DIR, 'media', 'KMC_Student_Database.xlsx')  # Use absolute path
            updated_df.to_excel(updated_excel_path, index=False)  # Save the updated dataframe
            
            return redirect('database')  # Redirect to the student list view

    else:
        form = CreateStudentForm()
    return render(request, 'myapp/createstudent.html', {'form': form})

def updatestudent_view(request):
    message = ''
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        update_form = UpdateStudentForm(request.POST)

        excel_path = os.path.join(settings.BASE_DIR, 'media', 'KMC_Student_Database.xlsx')  # Use absolute path
        df = pd.read_excel(excel_path)  # Load your dataframe

        if 'search' in request.POST and search_form.is_valid():
            student_data = get_student(df, search_form.cleaned_data['id'])
            if student_data:
                update_form = UpdateStudentForm(initial=student_data)
            else:
                message = 'Student not found.'
                update_form = UpdateStudentForm()

        elif 'update' in request.POST and update_form.is_valid():
            kwargs = update_form.cleaned_data
            barcode = kwargs.pop('barcode')  # Remove barcode and use it as the first argument

            updated_df = update_student(df, barcode, **kwargs)
            updated_excel_path = os.path.join(settings.BASE_DIR, 'media', 'KMC_Student_Database.xlsx')  # Use absolute path
            updated_df.to_excel(updated_excel_path, index=False)  # Save the updated dataframe
                
            return redirect('database')  # Redirect to the student list view
    else:
        search_form = SearchForm()
        update_form = UpdateStudentForm()
    return render(request, 'updatestudent.html', {'search_form': search_form, 'update_form': update_form, 'message': message})

def deletestudent_view(request):
    if request.method == 'POST':
        delete_form = DeleteForm(request.POST)
        if delete_form.is_valid():
            excel_path = os.path.join(settings.BASE_DIR, 'media', 'KMC_Student_Database.xlsx')  # Use absolute path
            df = pd.read_excel(excel_path)  # Load your dataframe
            id = delete_form.cleaned_data['id']
            
            updated_df = delete_student(df, id)
            updated_excel_path = os.path.join(settings.BASE_DIR, 'media', 'KMC_Student_Database.xlsx')  # Use absolute path
            updated_df.to_excel(updated_excel_path, index=False)  # Save the updated dataframe
            
            return redirect('database')  # Redirect to the student list view

    else:
        form = DeleteForm()
    return render(request, 'myapp/deletestudent.html', {'delete_form': form})
