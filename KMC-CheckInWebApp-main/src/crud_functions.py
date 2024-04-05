#Import pandas library
import pandas as pd
import matplotlib.pyplot as plt
from email.message import EmailMessage
from email.mime.application import MIMEApplication
import smtplib
from studenttypes import Student, Student_check



#Create Function (Parameters=Student)
def create_student(df, barcode, id, email, student_class, instructor, name, role, department, institution, service, caseName):
    
    #Check if barcode is just numbers
    if not str(barcode).isdigit():
        return 
    
    #Create the new student using student class
    new_student = Student(barcode, id, time_in, date, email, student_class, instructor, name, role, department, institution, service, caseName)
    #Student Dictionary, this is used to append it to each column in the excel sheet.
    student_dict = new_student.__dict__

    #This creates the new student and appends it to the next available row in the excel file
    updated_df = df._append(student_dict, ignore_index=True)
    #Creates a new updated excel
    updated_df.to_excel("student_data_updated.xlsx", index=False)
    #returns the updated dataframe so you can continue making changes
    return updated_df

#Create Function (Parameters=Student_check)
def create_student_check(df, barcode, id, time_in, date, email, student_class, instructor, name, role, department, institution, service, caseName):
    
    #Check if barcode is just numbers
    if not str(barcode).isdigit():
        return 
    
    #Create the new student using student class
    new_student = Student_check(barcode, id, time_in, date, email, student_class, instructor, name, role, department, institution, service, caseName)
    #Student Dictionary, this is used to append it to each column in the excel sheet.
    student_dict = new_student.__dict__

    #This creates the new student and appends it to the next available row in the excel file
    updated_df = df._append(student_dict, ignore_index=True)
    #Creates a new updated excel
    updated_df.to_excel("student_data_updated.xlsx", index=False)
    #returns the updated dataframe so you can continue making changes
    return updated_df

#Read Function
#print all names from column 'name'
def get_names(df): 
    print(df['name'])

#find student by id in the dataframe, print student info
def get_student(df, student_id):
    print("Searching for student...")
    student =  df.loc[df['id'] == student_id]
    if student.empty:
        print("No matches found")
    else:
        print(student)
    print("Search complete")

#Update Function 
def update_student(df, identifier, **kwargs):#unknown variables
    #Validate Data before updating
    # Check if identifier exists in the frame
    if not any(df['barcode'] == identifier):
        print("Student not found.")
        return df

    #Update existing student in excel
    index = df.index[df['barcode'] == identifier][0] #...
    for key, value in kwargs.items():
        if key in df.columns:
            df.at[index, key] = value #create index 
        else:
            print(f"Ignoring unknown value: {key}")

            #return print statment ignoring invalid key?
            ##print("Ignoring unknown value.."")
    # save changes back to the Excel file
    df.to_excel('student_data_updated.xlsx', index=False)

    print("Student information updated successfully.")
    return df

#Delete Function
def delete_student(df, identifier):
     # Check if identifier exists in the frame
    if not any(df['barcode'] == identifier):
        print("Student not found.")
        return df
    #Remove student based on certain value like barcode name etc.
    index = df.index[df['barcode'] == identifier][0]
    df = df.drop(index)

    # save changes back to the Excel file
    df.to_excel('student_data_updated.xlsx', index=False)

    print("Student deleted successfully.")
    return df

