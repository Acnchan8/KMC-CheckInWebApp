#Import libaries

#Create Student Class

#Create Function

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

#Saves excel file as a CSV for easy importing to google sheets
def save_daily_CSV(df):
    # Exclude the first row
    df_to_save = df.iloc[1:].reset_index(drop=True)
    #Sets the file path 
    file_path = "C:\\Users\\pc\\Downloads\\daily_log.csv"
    #Creates a csv file with the excel file data
    df_to_save.to_csv(file_path, index=False)

#Saves a specific class's attendance as a pdf
def save_specific_class_daily(df, specified_class):
    #Sets the file path 
    file_path = "C:\\Users\\pc\\Downloads\\daily_class_log.pdf"
    #Creates a dataframe with only students from the specified class
    filtered_df = df[df["student_class"] == specified_class]
    
    # Create a figure and a single subplot
    fig, ax = plt.subplots(figsize=(11, len(filtered_df)))
    #Hide axes
    ax.axis("off")

    #Create the table with the filtered dataframe
    chart = ax.table(cellText = filtered_df.to_numpy(), colLabels = filtered_df.columns.tolist(), loc='center', cellLoc='center', rowLoc='center')

    # Adjust the font size of the table here
    chart.set_fontsize(10)
    chart.auto_set_column_width(col=list(range(len(filtered_df.columns))))

    # Save the figure as a PDF
    plt.savefig(file_path)

    # Clear the figure to free memory, especially important if calling this function multiple times
    plt.close(fig)

#Send an email with a PDF attachment (Only works if you have 2 step authentication with google)
def send_email_with_pdf_attachment(send_from, send_from_password, send_to, specified_class, pdf_file_path):
    #Gmail -> smtp.gmail.com
    #Outlook -> smpt.office365.com
    #Yahoo -> smtp.mail.yahoo.com
    smtp_server = "smtp.gmail.com"

    #SSL -> 465 (Security is established before data is exchanged)
    #STARTTLS -> 587 (Encryption is after both client and server supports)
    smtp_port = 465

    #Your full email address
    smtp_user = send_from

    #Your email address password sort of
    #Go to manage account settings of your google account
    #Go to security, then go to 2-step verification and at the bottom app passwords
    #The app password created (should be 16 characters will be the password you input as your email password)
    smtp_password = send_from_password

    # Extract name from email address (before the '@')
    recipient_name = send_to.split('@')[0]

    # Email subject includes specified class and date
    subject = f"{specified_class} Attendance"

    # Custom message body
    message_body = f"""
        Hello {recipient_name},

        This is an automated email sent by python. The PDF attached to this message contains information about your class attendance.

        Thank you,
        Code Society
    """

    # Create the email message
    msg = EmailMessage()
    msg["From"] = send_from
    msg["To"] = send_to
    msg["Subject"] = subject
    msg.set_content(message_body)

    # Read the PDF file's content
    with open(pdf_file_path, 'rb') as file:
        pdf_content = file.read()
        #Names the pdf  attachment according to the filepath
        pdf_name = pdf_file_path.split('/')[-1]
        #Attaches the pdf to the message
        msg.add_attachment(pdf_content, maintype = "application", subtype = "pdf", filename = pdf_name)

    # Send the email via SMTP
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_user, smtp_password)
        server.send_message(msg)

    print(f"Email sent to {send_to} with attachment test3-30-24")
