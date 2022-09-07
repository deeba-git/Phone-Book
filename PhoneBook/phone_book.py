#Phone Book

import json
import os

print("For add new number, enter 'yes'?")
print("For find a saved number, enter 'Find'?: ")

user = input("Enter answer: ") #Taking a user input

#Defining a function for taking a contact details from user
def get_details():
    global contact_name, country_code, number
    contact_name = (input("Enter a name: "))
    country_code = input("Enter a country code: ")
    number = input("Enter a phone number: ")

#Defining a function for storing and appending details in .json file
def append_contact(filename = "phone_book.json"):
    if os.path.exists(filename): # 'os.path.exists()' means we checking .json file exists or not, if Yes then loads it and append it
        with open(filename, "r") as file: #Opening a file in 'read(r)' mode
            data = file.read() #Reading a file and storing into 'data' 
            json_data = json.loads(data) #loads a json file i.e. 'phone_book.json', as passing string 'data' inside loads()
            
        with open(filename, "w") as new_file:  #Opening a file in 'writing(w)' mode
            entry = {"Name" : contact_name, "Country_code" : country_code, "Number": number}
            json_data["PhoneBook"].append(entry)
            json.dump(json_data, new_file, indent=3) #appending/writing a details in .json file
    else:
        '''If .json file doesn't exist, then it creates a .json file i.e. 'phone_book.json' with 
        empty list and store the details in it'''
        with open(filename, "w") as json_file:
            json_list = { "PhoneBook" : [] } #Creates a empty list in .json file, NOTE: Don't create empty .json file
            entry = {"Name" : contact_name, "Country_code" : country_code, "Number": number}
            json_list["PhoneBook"].append(entry)
            json.dump(json_list, json_file, indent=3) #appending/writing a details in .json file

#Defining a funtion to find details from .json file by user input
def find_contact_from_json(filename = "phone_book.json"):
    with open(filename, "r") as file:
        data = file.read() #It's important to read the file first, when we have to loads() the .json file
        data_json =json.loads(data)
        find = input("Enter a name to find: ") #Taking a name as input to find respective details

    for keyval in data_json["PhoneBook"]: #Iterating through json file
        if find.lower() == keyval["Name"].lower(): #If searched name it equal to the name in json file than prints respective details
            print("Searched name: ", keyval["Name"])
            print("Country code: ", keyval["Country_code"])
            print("Phone number: ", keyval["Number"])
            break
    else:
        print("Not found in PhoneBook!")


def storing_finding_details():
    if user == "Yes":
        while True:
            get_details()
            append_contact()
            print("Sucessfully saved in 'Phone_Book'!")
            print("Want to add another number?")

            again = input("Yes or No: ")   
            if again != "Yes":
                print("Okay, Thanks!")
                break
    elif user == "Find":
        find_contact_from_json()
    else:
        print("Wrong, answer!, It should be either 'Yes' or 'Find'")
storing_finding_details()



    


