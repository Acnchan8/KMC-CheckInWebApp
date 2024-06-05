#Import functions from functions.py
import pandas as pd
import crud_functions as fc
import download_send as ds
import time

#Create Main
def main(): 
    time_in = time.monotonic()

    print(time_in)

    file_path = "tests\KMC_Student_Database.xlsx"
    df = pd.read_excel(file_path)
    
    check_in_df = pd.read_excel("tests\KMC_Master_Checkin.xlsx")

    #Creates a new student
    #df = fc.create_student_database(df, 156234, 132521, "schar@ucsd.edu", "Astro Medicine 101", "Athena", "Satoshi", "Frontend Developer", "Medical Physics", "University of California, San Diego", "Planet Doctor", "Mars lost a moon")
    #Updates an existing student's information
    #df = fc.update_student(df, 734628, instructor="new_instructor")
    #Deleted an existing student
    #df = fc.delete_student(df, 156234)

    #Processes a student check in
    #check_in_df = fc.process_student_check_in(df, 633647)
    #check_in_df = fc.process_student_check_in(df, 421305)
    #check_in_df = fc.process_student_check_in(df, 734628)
    #check_in_df = fc.process_student_check_in(df, 825739)
    #check_in_df = fc.process_student_check_in(df, 168162)

    time_in = time.monotonic()

    print(time_in)

    #for barcode in df['barcode']:
        #fc.process_student_check_in(df, barcode)
    
    #fc.get_names(df)
    #fc.get_student(df, "749309")
    check_in_df = pd.read_excel("tests\KMC_Master_Checkin.xlsx")
    ds.save_specific_class_daily(check_in_df, "Anatomy 101")

    # Note: To use send_email_with_pdf_attachment, you need to add your sender email, sender password, 
    # receiver email, and specified class as parameters. FilePath is already included as a parameter.
    ds.send_email_with_pdf_attachment("alvexin2@gmail.com", "qivf tuju jlvx ibsm ", "alvexin@gmail.com", "Anatomy 101", "tests\daily_class_log.pdf")

if __name__ == "__main__":
    main()
