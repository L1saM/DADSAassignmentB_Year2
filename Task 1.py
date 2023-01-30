# PROGRAM DESCRIPTION
# STUDENT NUMBER: 18004854
# LAST EDITED 17/04/2021
# MODULES NEEDED : CSV
# **********************************************************************************************************************
# HOW THE PROGRAM FUNCTIONS:
# PROGRAM READS TEXT FROM A CSV FILE, WHICH IS STORED IN SAME FOLDER
# CSV FILES CONTAIN PATIENTS INFORMATION SUCH AS A ID NUMBER, DOB, SEX, HEIGHT
# WEIGHT, AND AILMENT.
# ALL PATIENTS BMIS' ARE CALCULATED USING A BMI FUNCTION
# PATIENTS ARE ALLOCATED INTO WEIGHT CLASSES OF OBESE, OVERWEIGHT, NORMAL AND UNDERWEIGHT
# PATIENTS ARE PUT INTO BMI ORDER STARTING WITH UNDERWEIGHT CLASS TO OVERWEIGHT CLASS
# 5 WORST UNDERWEIGHT AND 5 WORST OBESE PATIENTS ARE ALSO PRODUCED.
# **********************************************************************************************************************
# USING THE PROGRAM:
# A) DESIGN AND SAVE A SPREADSHEET CONTAINING PATIENT DATA
# B) NAME IT 'DADSA 2021 CWK B DATA COLLECTION.csv'
# C) ADD CSV FILES TO SAME FOLDER AS PROGRAM STORED
# D) PRESS RUN TO PRODUCE A OUTPUT
# E) STUDY OUTPUT RESULTS PRINTED
# **********************************************************************************************************************

# START

# importing csv module
import csv

# csv file name
filename = "DADSA 2021 CWK B DATA COLLECTION.csv"

# initializing the columns and rows list
columns = []
rows = []

########################################################################################################################

# Function: patient_bmi.
# Uses: Used to calculate each patients BMI and assign them to a weight class category.
# Calculation for bmi is: bmi = weight / (height ** 2).

def patient_bmi(bmi):
    # BMI calculation of weight divided by height multiplied by height.

    # If the patient has a bmi of over 30 then class them as obese
    if bmi >= 30:
        return "Obese"
    # If the patient has a bmi of up to 25 then class them as overweight
    elif bmi >= 25:
        return "Overweight"
    # If the patient has a bmi of over 18.5 then class them as normal
    elif bmi >= 18.5:
        return "Normal"
    # If the patient has a bmi of up to 18.5 then class them as normal
    elif bmi < 18.5:
        # If the patient has a bmi of lower than 18.5 then class them as underweight
        return "Underweight"

########################################################################################################################

# importing datetime module
from datetime import date
# Patients ages from DOB

# Function: calculate_age.
# Uses: calculates the patients age based on dob.

def calculate_age(dateOfBirth):
    # Calculates todays date
    today = date.today()
    #print(today.year)
    # Patients DOB split with / i.e. dd/mm/yyyy
    dob = dateOfBirth.split('/')
    #print(dob)
    #When importing THE DOB from CSV, convert to a string from a float. Using str(dob). Then convert str to int.
    birth_date = date(int(dob[2]), int(dob[1]), int(dob[0]))
    # Minus' patients birth year from current year to work out age
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    return age

########################################################################################################################

# Function: sorting_patient_weight.
# Uses: Sorts the patients weight into weight categories and displays them.

def sorting_patient_weight(arr):
    sorting = [[], [], [], []]
    for i in range(len(arr)):
        if "Obese" in arr[i]:
            sorting[0].append(arr[i])
        elif "Underweight" in arr[i]:
            sorting[1].append(arr[i])
        elif "Overweight" in arr[i]:
            sorting[2].append(arr[i])
        elif "Normal" in arr[i]:
            sorting[3].append(arr[i])

    rows = []
    for item in sorting:
        rows.extend(item)

    return rows

########################################################################################################################

# Function: patient_sex.
# Uses: Separated the two patient sexes listed on the csv and displays them in groups.

def patient_sex(array):
    for j in range(len(array)):
        #Obese Female
        if "Obese" in array[j]:
            if "F" in array[j]:
                print("\n Female top 5 obese category are: ")
                print("Patient name: " + patient_list[j][0] + " , Patient Age: " + str(
                    patient_list[j][1]) + " , BMI: " + str(patient_list[j][10]) + " , Weight class : " +
                      patient_list[j][11])
                #Underweight Female
        if "Underweight" in array[j]:
            if "F" in array[j]:
                print("\n Female top 5 underweight category are: ")
                print("Patient name: " + patient_list[j][0] + " , Patient Age: " + str(
                    patient_list[j][1]) + " , BMI: " + str(patient_list[j][10]) + " , Weight class : " +
                      patient_list[j][11])
    print("-----------------------------------------------------------------------------------------------------------")

    for j in range(len(array)):
        #Obese male
        if "Obese" in array[j]:
            if "M" in array[j]:
                print("\n Male top 5 Obese category are: ")
                print("Patient name: " + patient_list[j][0] + " , Patient Age: " + str(
                    patient_list[j][1]) + " , BMI: " + str(patient_list[j][10]) + " , Weight class : " +
                      patient_list[j][11])
                #Underweight Male
        if "Underweight" in array[j]:
            if "M" in array[j]:
                print("\n Male top 5 underweight category are: ")
                print("Patient name: " + patient_list[j][0] + " , Patient Age: " + str(
                    patient_list[j][1]) + " , BMI: " + str(patient_list[j][10]) + " , Weight class : " +
                      patient_list[j][11])
    print("------------------------------------------------------------------------------------------------------------")

########################################################################################################################

# Loading in CSV file to be used

# reading csv file using open function
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row 
    columns = next(csvreader)

    # extracting each data row one by one for patient BMI
    for row in csvreader:
        # Index of height and weight in the CSV file
        bmi = (int(row[4])) / (float(row[3]) ** 2)
        weight_class = patient_bmi(bmi)
        row[-2] = round(bmi, 1)
        row[-1] = weight_class
        rows.append(row)
        # Reading patients dob from csv file
        age = calculate_age(str(row[1]))
        row[1] = age

########################################################################################################################

        # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

# printing the column names
print('Column names are : ' + ', '.join(field for field in columns))

#  printing all the rows
print('\n Patients data is as follows :\n')

########################################################################################################################

patient_list = sorting_patient_weight(rows)

# Function: Patient_counter.
# Uses: Creates a gap for every 10 patients to make it more readable when the user presses enter.
patient_counter = 0
for i in range(0, len(patient_list)):

    #Counts every 10 patients
    if patient_counter == 10:
        end = False
        while end == False:
            patient_counter = 0
            #Prompts user, adds new lines for clarity
            input("\n Press the enter button ------------->\n")
            end = True
    # String concatenation
    print("Patient name: " + patient_list[i][0] + " , Patient Age: " + str(patient_list[i][1]) + " , BMI: " + str(patient_list[i][10]) + " , Weight class : " + patient_list[i][11])
    #Prints 10 rows of patients information
    patient_counter = patient_counter + 1

    print("------------------------------------------------------------------------------------------------------------")

print(patient_sex(patient_list))

########################################################################################################################

#END
