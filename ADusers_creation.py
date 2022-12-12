# Zakaria Ahmed
from passwordgenerator import pwgenerator
import csv
def header():
    headerList = ['Name','username','passcode','Title',]

    # open CSV file and assign header
    with open("users.csv", 'w',newline='') as file:
        dd = csv.DictWriter(file, delimiter=',',
                            fieldnames=headerList)
        dd.writeheader()
def add_user():
    infile = open("users.csv", "a")
    Name = str((input('enter your full name:')))
    username = str((input('enter your username:')))
    passcode = pwgenerator.generate()
    Title = str((input('enter your job title:')))

    data1 = f"\n{username},{passcode},{Name},{Title}"
    data = data1.strip() # strips white space
    infile.write(data +"\n") # appends to new line
    print('record added succesfully !')
    infile.close()
   
def gen_user():
    p = subprocess.Popen(["powershell.exe",
                          "C:\\Users\\Administrator\\Desktop\\AD_Users.ps1"],
                         stdout=sys.stdout)
    p.communicate()
    
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
        elif  choice == "q":
            break

        else: print('Invalid choice!')
main()# calls all the code
