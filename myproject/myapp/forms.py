from django import forms

class CreateStudentForm(forms.Form):
    barcode = forms.CharField(label='Barcode', max_length=255, required=False)
    id = forms.CharField(label='ID', max_length=255, required=False)
    email = forms.EmailField(label='Email', max_length=255, required=False)
    student_class = forms.CharField(label='Student Class', max_length=255, required=False)
    instructor = forms.CharField(label='Instructor', max_length=255, required=False)
    name = forms.CharField(label='Name', max_length=255, required=True)
    role = forms.CharField(label='Role', max_length=255, required=False)
    department = forms.CharField(label='Department', max_length=255, required=False)
    institution = forms.CharField(label='Institution', max_length=255, required=False)
    service = forms.CharField(label='Service', max_length=255, required=False)
    caseName = forms.CharField(label='Case Name', max_length=255, required=False)

class SearchForm(forms.Form):
    id = forms.CharField(label='ID', max_length=255, required=False)

class UpdateStudentForm(forms.Form):
    barcode = forms.CharField(label='Barcode', max_length=255, required=False)
    id = forms.CharField(label='ID', max_length=255, required=False)
    email = forms.EmailField(label='Email', max_length=255, required=False)
    student_class = forms.CharField(label='Student Class', max_length=255, required=False)
    instructor = forms.CharField(label='Instructor', max_length=255, required=False)
    name = forms.CharField(label='Name', max_length=255, required=True)
    role = forms.CharField(label='Role', max_length=255, required=False)
    department = forms.CharField(label='Department', max_length=255, required=False)
    institution = forms.CharField(label='Institution', max_length=255, required=False)
    service = forms.CharField(label='Service', max_length=255, required=False)
    caseName = forms.CharField(label='Case Name', max_length=255, required=False)

class DeleteForm(forms.Form):
    id = forms.CharField(label='ID', max_length=255, required=False)