#Import pandas library
import pandas as pd
import matplotlib.pyplot as plt
from email.message import EmailMessage
from email.mime.application import MIMEApplication
import smtplib
from datetime import datetime

class Student:
    def __init__(self, barcode, id, email, student_class, instructor, name, role, department, institution, service, caseName):
        self.barcode = barcode
        self.id = id
        self.email = email
        self.student_class = student_class
        self.instructor = instructor
        self.name = name
        self.role = role
        self.department = department
        self.institution = institution
        self.service = service
        self.caseName = caseName

class StudentCheck:
    def __init__(self, barcode, id, time_in, date, email, student_class, instructor, name, role, department, institution, service, caseName):
        self.barcode = barcode
        self.id = id
        self.time_in = time_in
        self.date = date
        self.email = email
        self.student_class = student_class
        self.instructor = instructor
        self.name = name
        self.role = role
        self.department = department
        self.institution = institution
        self.service = service
        self.caseName = caseName

#Create Function Database(Parameters=Student)
def create_student_database(df, barcode, id, email, student_class, instructor, name, role, department, institution, service, caseName):
    barcode = str(barcode)
    print("Barcode: ", barcode)
    #Check if barcode is just numbers
    if not str(barcode).isdigit() and not len(str(barcode)) == 0:
        print("Invalid barcode. Barcode should be numeric.")
        return df
    
    existing_barcodes = df['barcode'].astype(str).values
    print("Existing barcodes in DataFrame:", existing_barcodes)

    # Check if barcode exists in the frame
    if barcode in existing_barcodes:
        print("Student barcode found.")
        return df
    
    #Create the new student using student class
    new_student = Student(barcode, id, email, student_class, instructor, name, role, department, institution, service, caseName)
    #Student Dictionary, this is used to append it to each column in the excel sheet.
    student_dict = new_student.__dict__

    #This creates the new student and appends it to the next available row in the excel file
    updated_df = df._append(student_dict, ignore_index=True)
    #Creates a new updated excel
    updated_df.to_excel("media\KMC_Student_Database.xlsx", index=False)
    #returns the updated dataframe so you can continue making changes
    print("Student information added successfully.")

    return updated_df

#Update Function Database
#**kwargs allows you to pass any number of arguments to a function
def update_student(df, barcode, **kwargs):#unknown variables
    try:
        barcode = int(barcode)  # Convert to integer if it's a numeric string
    except ValueError:
        print("Invalid barcode format. barcode should be numeric.")
        return None

    #Validate Data before updating
    # Check if barcode exists in the frame
    if not any(df['barcode'] == barcode):
        print("Student not found.")
        return df

    #Update existing student in excel
    index = df.index[df['barcode'] == barcode][0] #...
    for key, value in kwargs.items():
        if key in df.columns:
            df.at[index, key] = value #create index 
        else:
            print(f"Ignoring unknown value: {key}")

            #return print statment ignoring invalid key?
            ##print("Ignoring unknown value.."")
    # save changes back to the Excel file
    df.to_excel('media\KMC_Student_Database.xlsx', index=False)

    print("Student information updated successfully.")
    return df

#Delete Function
def delete_student(df, id):
    try:
        id = int(id)  # Convert to integer if it's a numeric string
    except ValueError:
        print("Invalid id format. id should be numeric.")
        return None

    # Check if id exists in the frame
    if not any(df['id'] == id):
        print("Student not found.")
        return df
    #Remove student based on certain value like id name etc.
    index = df.index[df['id'] == id][0]
    df = df.drop(index)

    # save changes back to the Excel file
    df.to_excel('media\KMC_Student_Database.xlsx', index=False)

    print("Student deleted successfully.")
    return df

def process_student_check_in(df, barcode):
    #file path of check in sheet
    file_path = "myproject\media\KMC_Master_Checkin.xlsx"
    student_check_in_df = pd.read_excel(file_path)
    # Check if the barcode is valid and exists in the DataFrame
    if barcode not in df['barcode'].values:
        print(f"No student found with barcode {barcode}.")
        return df
    
    # Extract student data using the barcode
    # Get the current time and date
    time_in = datetime.now().strftime("%H:%M:%S")
    date = datetime.now().strftime("%Y-%m-%d")
    
    student_data = df[df['barcode'] == barcode].iloc[0]

    #Create the new student using student class
    new_student = StudentCheck(
        barcode=student_data['barcode'],
        id=student_data['id'],
        time_in=time_in,
        date=date,
        email=student_data['email'],
        student_class=student_data['student_class'],
        instructor=student_data['instructor'],
        name=student_data['name'],
        role=student_data['role'],
        department=student_data['department'],
        institution=student_data['institution'],
        service=student_data['service'],
        caseName=student_data['caseName']
    )
    #Student Dictionary, this is used to append it to each column in the excel sheet.
    student_dict = new_student.__dict__

    #This creates the new student and appends it to the next available row in the excel file
    student_check_in_df = student_check_in_df._append(student_dict, ignore_index=True)
    #Creates a new updated excel
    student_check_in_df.to_excel(file_path, index=False)
    #returns the updated dataframe so you can continue making changes
    return student_check_in_df

#Read Function
#print all names from column 'name'
def get_names(df): 
    print(df['name'])

#find student by id in the dataframe, print student info
def get_student(df, student_id):
    print("Searching for student...")
    try:
        student_id = int(student_id)  # Convert to integer if it's a numeric string
    except ValueError:
        print("Invalid ID format. ID should be numeric.")
        return None
    print(student_id)
    print(df['id'])
    student = df.loc[df['id'] == student_id]
    if student.empty:
        print("No matches found")
        return None
    else:
        # Convert the first (and should be only) row of DataFrame to a dictionary
        student_data = student.iloc[0].to_dict()
        return student_data