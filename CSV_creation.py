# Zakaria Ahmed
import pandas as pd
import csv

def header():
    headerList = ['firstname', 'lastname', 'username', 'email','StreetAddress','City','ZipCode','State','Country']

    # open CSV file and assign header
    with open("students.csv", 'w') as file:
        dd = csv.DictWriter(file, delimiter=',',
                            fieldnames=headerList)
        dd.writeheader()
#import paramiko
def add_user():
    infile = open("students.csv", "a")
    first_last_name = str((input('enter your first_last_name:')))
    last_name = str(input('enter your last_name:'))
    phone = str(input('what is your phone number:'))
    office = str(input('which office are you in:'))
    title = input('what is your title:')
    account_name = input('what is your account name:')

    data1 = f"\n{first_last_name},{last_name},{office},{phone},{title},{account_name}"
    data = data1.strip() # strips white space
    infile.write(data +"\n") # appends to new line
    print('record added succesfully !')
    infile.close()


def main():

    print('Welcome to CSV creation')
    print('********************************************************'
        ' **  \n'
        ' **	Please choose one of the options below:\n'
        ' **	[a] to add new student record\n'
        ' **	[h] to initialze headers\n'  
        ' **	[q] to quit \n'
        ' ********************************************************\n')
    choice = input('pick:')
    while True:
        if choice == "a":
            add_user()
            break
        elif choice == "h":
            header()
            break
        elif  choice == "q":
            break

        else: print('Invalid choice!')




main()# calls all the code
