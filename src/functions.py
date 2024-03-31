#Import libaries

#Create Student Class

#Create Function

#Read Function

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

#Save Daily CSV Function

#Save Specific Class Daily Function

#Send Email Function
