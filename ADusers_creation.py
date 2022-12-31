import csv
import subprocess, sys
from password_generator import password_generator
from sending import email_credentials
def header():
    headerList = ['FirstName', 'LastName', 'passcode', 'Title', 'Manager_Email']

    # open CSV file and assign header
    with open("users.csv", 'w', newline='') as file:
        dd = csv.DictWriter(file, delimiter=',',
                            fieldnames=headerList)
        dd.writeheader()

def add_user():
    while True:
        infile = open("users.csv", "a")
        First_name = str((input('enter the first name:')))
        Last_name = str((input('enter the last name:')))
        passcode = password_generator()
        Title = str((input('enter the job title:')))
        Manager_Email = str((input('enter the Managers email:')))
        data1 = f"\n{First_name},{Last_name},{passcode},{Title},{Manager_Email}"
        data = data1.strip()  # strips white space
        infile.write(data + "\n")  # appends to new line
        infile.close()
        print('record added succesfully !')

        choice = input('would you like to add another user Y/N')
        if choice == 'N':
            break
        elif choice == 'Y':
            continue
        else:
            print('"Invalid input.\nExiting."')
            exit(1)
def gen_user():
    p = subprocess.Popen(["powershell.exe",
                          "C:\\Users\\Administrator\\Desktop\\AD_Users.ps1"],
                         stdout=sys.stdout)
    p.communicate() # implent logging
    choice = input('would you like to email the managers the credentials[Y]:')
    if choice == 'Y':
        email_credentials()
    else:
        print('users have been generated check the console for errors')


def main():
    print('Welcome to AD_USERS creation')
    print('********************************************************'
          ' **  \n'
          ' **	Please choose one of the options below:\n'
          ' **	[a] to add new AD user record\n'
          ' **	[h] to initialze headers\n'
          ' **	[G] to generate users \n'
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
        elif choice == "G":
            gen_user()
            break
        elif choice == "q":
            break

        else:
            print('Invalid choice!')
main()  # calls all the co
