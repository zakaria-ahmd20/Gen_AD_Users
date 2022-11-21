# Zakaria Ahmed
import csv

def header():
    headerList = ['username','passcode']

    # open CSV file and assign header
    with open("students.csv", 'w',newline='') as file:
        dd = csv.DictWriter(file, delimiter=',',
                            fieldnames=headerList)
        dd.writeheader()



def add_user():
    infile = open("students.csv", "a")
    username = str((input('enter your username:')))
    passcode = "Nike123_"


    data1 = f"\n{username},{passcode}"
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
