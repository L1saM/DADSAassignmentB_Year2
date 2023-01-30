# PROGRAM DESCRIPTION
# STUDENT NUMBER: 18004854
# LAST EDITED 20/04/2021
# MODULES NEEDED : CSV
# ****************************************************************************#
# HOW THE PROGRAM FUNCTIONS:
# PROGRAM READS TEXT FROM A CSV FILE, WHICH IS STORED IN SAME FOLDER
# CSV FILES CONTAIN PATIENTS INFORMATION SUCH AS A ID NUMBER, DOB, SEX, HEIGHT
# WEIGHT, AND AILMENT.
# ALL PATIENTS BMIS ARE CALCULATED USING A BMI FUNCTION
# PATIENTS ARE RANKED ACCORDING TO PROVIDED RULES IN SPEC
# PATIENTS ARE DETERMINED WHETHER THEY NEED TO BE REFERRED TO DIETITIAN
# PRIORITY ORDER OF REFERRED PATIENTS IS PRODUCED IN ORDER
# *****************************************************************************
# USING THE PROGRAM:
# A) DESIGN AND SAVE A SPREADSHEET CONTAINING PATIENT DATA
# B) NAME IT 'DADSA 2021 CWK B DATA COLLECTION.csv'
# C) ADD CSV FILES TO SAME FOLDER AS PROGRAM STORED
# D) PRESS RUN TO PRODUCE A OUTPUT
# E) STUDY OUTPUT RESULTS PRINTED
# *****************************************************************************

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

# importing datetime module.
from datetime import date
# Patients ages from DOB.

# Function: calculate_age.
# Uses: calculates the patients age based on dob provided.

def calculate_age(dateOfBirth):
    # Calculates todays current date
    today = date.today()
    # Patients DOB split with / i.e. dd/mm/yyyy
    dob = dateOfBirth.split('/')
    #When importing THE DOB from CSV, convert to a string from a float. Using str(dob). Then convert str to int.
    birth_date = date(int(dob[2]), int(dob[1]), int(dob[0]))
    # Minus' patients birth year from current year to work out age
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    return age

########################################################################################################################

# Function: sort_patient_array.
# Uses: Sorts the patients in the array based on their age.

def sort_patient_age(array):
    #Sorts patients in the array based on age
    n = len(array)
    for z in range(n-1):
        for x in range(0, n-z-1):
            if array[x][1] < array[x+1][1]:
                array[x], array[x+1] = array[x+1], array[x]

########################################################################################################################

# Function: sorting_patient_weight.
# Uses: Sorts the patients weight into weight categories and displays them.

def sorting_patient_weight(arr):
    # Patient list
    sorting = [[], [], [], []]
    for i in range(len(arr)):
        # Obese weight class
        if "Obese" in arr[i]:
            sorting[0].append(arr[i])
            # Underweight weight class
        elif "Underweight" in arr[i]:
            sorting[1].append(arr[i])
            # Overweight weight class
        elif "Overweight" in arr[i]:
            sorting[2].append(arr[i])
            # Normal weight class
        elif "Normal" in arr[i]:
            sorting[3].append(arr[i])

# Sorts through patients ages running from oldest - youngest in each weight class
    sort_patient_age(sorting[0])
    sort_patient_age(sorting[1])
    sort_patient_age(sorting[2])
    sort_patient_age(sorting[3])
    rows = []
    for item in sorting:
        rows.extend(item)

    return rows

########################################################################################################################

# Function: patient_referral.
# Uses: Identifies patients needing to be referred to dietitian following criteria.

def patient_referral(array):
    # Patients needing to be referred
    refer = []
    for j in range(len(array)):
        # Patients conditions
        if "Obese" in array[j] or "Underweight" in array[j]:
            if "refer" not in array[j]:
                array[j].append("refer")
                refer.append(array[j])
                #Referral for Hypertension
        if "Hypertension" in array[j]:
            if "refer" not in array[j]:
                array[j].append("refer")
                refer.append(array[j])
                # Referral for asthma/ smoker
        if "Asthmatic" in array[j] or "smoker" in array[j]:
            if "refer" not in array[j]:
                array[j].append("refer")
                refer.append(array[j])
                # Referral for Renal RT
        if "Renal RT" in array[j]:
            if "refer" not in array[j]:
                array[j].append("refer")
                refer.append(array[j])
                # Referral for Ileostomy/Colostomy
        if "Ileostomy / Colostomy" in array[j]:
            if "refer" not in array[j]:
                array[j].append("refer")
                refer.append(array[j])
                # Referral for Parenteral nutrition
        if "Parenteral nutrition" in array[j]:
            if "refer" not in array[j]:
                array[j].append("refer")
                refer.append(array[j])
                # Referral for NJT/NGR
        if "NJT/NGR" in array[j]:
            if "refer" not in array[j]:
                array[j].append("refer")
                refer.append(array[j])
    # Patients are referred with any one condition
    return refer

########################################################################################################################

# Function: Priority_level.
# Uses: Checks through the patients medical conditions and counts them. If a patient has more than 2 conditions,
# they are then marked as top priority.

def priority_level(array, iterate):
    top_priority = False
    counter = 0
    # Index rows for patients medical conditions
    for p in array[iterate][5:12]:
        if p != '':
            counter += 1
            # If patient has more than 2 conditions
            if counter > 2:
                # Marked as top priority
                top_priority = True

    return top_priority

########################################################################################################################

# Function: top_priority.
# Uses: Uses specific conditions to check if a patient meets the criteria to be referred, top priority or not referred.

def top_priority(arr):
    #Array of all the patients
    top_priority = []
    not_referred = []
    for i in range(len(arr)):
        # If patient asthmatic/smoker AND over 55 = top priority
        if arr[i][1] > 55 and ("Asthmatic" in arr[i] or "Smoker" in arr[i]):
            arr[i][-1] = "Top priority"
            top_priority.append(arr[i])
            # If weight class = obese AND have hypertension = top priority
        elif "Obese" in arr[i] and "Hypertension" in arr[i]:
            arr[i][-1] = "Top priority"
            top_priority.append(arr[i])
        elif priority_level(arr, i) == True:
            arr[i][-1] = "Top priority"
            top_priority.append(arr[i])
        else:
            not_referred.append(arr[i])

    return [top_priority, not_referred]

########################################################################################################################

# Function: Sort_by_age.
# Uses: Sorts patients by ages starting with the oldest patient.

def sort_by_age(array):
    # patient array
    sorted_array = []
    while len(array) > 0:
        # oldest patient in the list
        oldest = array[0]
        for x in range(len(array)):
            if array[x][1] > oldest[1]:
                oldest = array[x]
        sorted_array.append(oldest)
        array.remove(oldest)
    # Returns list of patients with oldest at the top
    return sorted_array

########################################################################################################################

# Loading in CSV file to be used.

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
        row.append (round(bmi, 1))
        row.append (weight_class)

        #Patients medical conditions
        if row[5] == "Y":
            # Y means patient is a smoker
            row[5] = "smoker"
        if row[6] == "Y":
            # Y means patient is asthmatic
            row[6] = "Asthmatic"
        if row[7] == "Y":
            # Y means patient has a NJT/NGR
            row[7] = "NJT/NGR"
        if row[8] == "Y":
            # Y means patient has hypertension
            row[8] = "Hypertension"
        if row[9] == "Y":
            # Y means patient has rental RT
            row[9] = "Renal RT"
        if row[10] == "Y":
            # Y means patient as a Ileostomy/ Colostomy
            row[10] = "Ileostomy / Colostomy"
        if row[11] == "Y":
            # Y means patient has Parenteral Nutrition
            row[11] = "Parenteral Nutrition"
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
print('\n Patients that need to be referred to a dietitian are as follows:\n')

########################################################################################################################

# Calling functions.

# Sorting patients
patient_list = sorting_patient_weight(rows)
# List of top priority patients
return_value = top_priority(patient_list)
# Returns top priority
top_refer = return_value[0]
# Patients not needing to be referred
not_referred = return_value[1]
refer = patient_referral(not_referred)
# Sorted by age
sorted_refer = sort_by_age(refer)
sorted_top = sort_by_age(top_refer)

########################################################################################################################

# Function: Patient_counter
# Uses: Creates a gap for every 10 patients to make it more readable when the user presses enter.

def patient_counter(array, counter):

    patient_counter = counter
    for i in range (len(array)):

        # Counts every 10 patients
        if patient_counter == 10:
            end = False
            while end == False:
                patient_counter = 0
                #Prompts user, adds new lines for clarity
                input("\n Press the enter button ------------->\n")
                end = True
        print(array[i])
        #Prints 10 rows of patients information
        patient_counter = patient_counter + 1

        print("-------------------------------------------------------------------------------------------------------")

    return patient_counter

count = patient_counter(sorted_top, 0)
patient_counter(sorted_refer, count)

########################################################################################################################

#END


