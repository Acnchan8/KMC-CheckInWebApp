
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .crud_functions import create_student_database, update_student, get_student, delete_student
from .download_send import save_specific_class_daily, send_email_with_pdf_attachment
from .forms import CreateStudentForm, SearchForm, UpdateStudentForm, DeleteForm, DownloadForm, EmailForm
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
    df = pd.read_excel(excel_path, dtype={'barcode': str, 'id': str})

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
            barcode = form.cleaned_data.get('barcode', 'N/A')
            id = form.cleaned_data.get('id', 'N/A')
            email = form.cleaned_data['email']  # Email is required, safe to access directly
            student_class = form.cleaned_data.get('student_class', 'N/A')
            instructor = form.cleaned_data.get('instructor', 'N/A')
            name = form.cleaned_data['name']  # Name is required, safe to access directly
            role = form.cleaned_data.get('role', 'N/A')
            department = form.cleaned_data.get('department', 'N/A')
            institution = form.cleaned_data.get('institution', 'N/A')
            service = form.cleaned_data.get('service', 'N/A')
            caseName = form.cleaned_data.get('caseName', 'N/A')
            
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
            id = delete_form.cleaned_data['id']
            excel_path = os.path.join(settings.BASE_DIR, 'media', 'KMC_Student_Database.xlsx')  # Use absolute path
            df = pd.read_excel(excel_path)  # Load your dataframe
            
            updated_df = delete_student(df, id)
            updated_excel_path = os.path.join(settings.BASE_DIR, 'media', 'KMC_Student_Database.xlsx')  # Use absolute path
            updated_df.to_excel(updated_excel_path, index=False)  # Save the updated dataframe
            
            return redirect('database')  # Redirect to the student list view

    else:
        delete_form = DeleteForm()
    return render(request, 'myapp/deletestudent.html', {'delete_form': delete_form})

def downloaddata_view(request):
    if request.method == 'POST':
        download_form = DownloadForm(request.POST)
        if download_form.is_valid():
            specific_class = download_form.cleaned_data['specific_class']
            excel_path = os.path.join(settings.BASE_DIR, 'media', 'KMC_Master_Checkin.xlsx')  # Use absolute path
            df = pd.read_excel(excel_path)  # Load your dataframe
            
            save_specific_class_daily(df, specific_class)
            
            return redirect('database')  # Redirect to the student list view

    else:
        download_form = DownloadForm()
    return render(request, 'myapp/downloaddata.html', {'download_form': download_form})

def emaildata_view(request):
    if request.method == 'POST':
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            send_to = email_form.cleaned_data['send_to']
            specific_class = email_form.cleaned_data['specific_class']
            excel_path = os.path.join(settings.BASE_DIR, 'media', 'KMC_Master_Checkin.xlsx')  # Use absolute path
            df = pd.read_excel(excel_path)  # Load your dataframe
            
            file_path = os.path.join(settings.MEDIA_ROOT, 'daily_log.pdf')
            send_email_with_pdf_attachment("alvexin2@gmail.com", "qivf tuju jlvx ibsm ", send_to, specific_class, file_path)
            
            return redirect('database')  # Redirect to the student list view

    else:
        email_form = EmailForm()
    return render(request, 'myapp/emaildata.html', {'email_form': email_form})
