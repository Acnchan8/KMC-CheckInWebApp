import smtplib
from email.message import EmailMessage

def send_email_with_excel_attachment(send_from, send_from_password, send_to, specified_class, excel_file_path):
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

    # Read the Excel file's content
    with open(excel_file_path, 'rb') as file:
        excel_content = file.read()
        excel_name = excel_file_path.split('/')[-1]
        msg.add_attachment(excel_content, maintype="application", subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename=excel_name)

    # Send the email via SMTP
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_user, smtp_password)
        server.send_message(msg)

    print(f"Email sent to {send_to} with attachment test3-30-24")



