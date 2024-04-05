#Import functions from functions.py
import pandas as pd
import CRUD_Functions as fc

#Create Main
def main(): 
    file_path = "C:\\Users\\pc\\Downloads\\KMC_Test_Students.xlsx"

    df = pd.read_excel(file_path)

    df = fc.create_student(df, "81598", "81598", "12/25/24 3:00pm", "test@email.edu", "student_class", "instructor", "name", "role", "department", "institution", "service", "caseName")
    df = fc.create_student(df, "56283", "81598", "12/25/24 3:00pm", "test@email.edu", "student_class", "instructor", "name", "role", "department", "institution", "service", "caseName")
    df = fc.create_student(df, "749309", "749309", "12/25/24 3:00pm", "test@email.edu", "student_class", "instructor", "name", "role", "department", "institution", "service", "caseName")

    fc.get_names(df)
    fc.get_student(df, "749309")

    fc.save_daily_CSV(df)

    fc.save_specific_class_daily(df, "student_class")

    # Note: To use send_email_with_pdf_attachment, you need to add your sender email, sender password, 
    # receiver email, and specified class as parameters. FilePath is already included as a parameter.
    fc.send_email_with_pdf_attachment("C:\\Users\\pc\\Downloads\\daily_class_log.pdf")

if __name__ == "__main__":
    main()
