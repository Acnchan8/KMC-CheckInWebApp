from django import forms
from django.core.exceptions import ValidationError

class CreateStudentForm(forms.Form):
    barcode = forms.CharField(label='Barcode', max_length=255, required=False)
    id = forms.CharField(label='ID', max_length=255, required=True)
    email = forms.EmailField(label='Email', max_length=255, required=True)
    student_class = forms.CharField(label='Student Class', max_length=255, required=False)
    instructor = forms.CharField(label='Instructor', max_length=255, required=False)
    name = forms.CharField(label='Name', max_length=255, required=True)
    role = forms.CharField(label='Role', max_length=255, required=False)
    department = forms.CharField(label='Department', max_length=255, required=False)
    institution = forms.CharField(label='Institution', max_length=255, required=False)
    service = forms.CharField(label='Service', max_length=255, required=False)
    caseName = forms.CharField(label='Case Name', max_length=255, required=False)

    def clean_barcode(self):
        barcode = self.cleaned_data.get('barcode')
        if barcode and not barcode.isdigit():
            raise ValidationError('Invalid barcode. Barcode should be numeric.')
        return barcode

    def clean_id(self):
        id = self.cleaned_data.get('id')
        if id and not id.isdigit():
            raise ValidationError('Invalid ID. ID should be numeric.')
        return id
    
class SearchForm(forms.Form):
    id = forms.CharField(label='ID', max_length=255, required=False)

    def clean_id(self):
        id = self.cleaned_data.get('id')
        if id and not id.isdigit():
            raise ValidationError('Invalid ID. ID should be numeric.')
        return id

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

    def clean_barcode(self):
        barcode = self.cleaned_data.get('barcode')
        if barcode and not barcode.isdigit():
            raise ValidationError('Invalid barcode. Barcode should be numeric.')
        return barcode

    def clean_id(self):
        id = self.cleaned_data.get('id')
        if id and not id.isdigit():
            raise ValidationError('Invalid ID. ID should be numeric.')
        return id

class DeleteForm(forms.Form):
    id = forms.CharField(label='ID', max_length=255, required=True)
    def clean_id(self):
        id = self.cleaned_data.get('id')
        if id and not id.isdigit():
            raise ValidationError('Invalid ID. ID should be numeric.')
        return id
    
class DownloadForm(forms.Form):
    specific_class = forms.CharField(label='Class', max_length=255, required=True) 

class EmailForm(forms.Form):
    send_to = forms.EmailField(label='Email To', max_length=255, required=True)
    specific_class = forms.CharField(label='Class', max_length=255, required=True) 
