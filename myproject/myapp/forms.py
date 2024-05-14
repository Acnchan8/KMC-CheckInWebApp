from django import forms

class StudentForm(forms.Form):
    barcode = forms.CharField(max_length=255)
    id = forms.CharField(max_length=255)
    email = forms.EmailField()
    student_class = forms.CharField(max_length=255)
    instructor = forms.CharField(max_length=255)
    name = forms.CharField(max_length=255)
    role = forms.CharField(max_length=255)
    department = forms.CharField(max_length=255)
    institution = forms.CharField(max_length=255)
    service = forms.CharField(max_length=255)
    caseName = forms.CharField(max_length=255)
