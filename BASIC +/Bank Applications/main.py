from sys import exit
from getpass import getpass
template = ["name", "pass", "balance"]
data = { 
    1001 : {
        "name" : "Sachin Yadav",
        "pass" : "radhat",
        "balance" : 50000
    },
    1002 : {
        "name" : "ram",
        "pass" : "Asimov",
        "balance" : 50000
    },
    1003 : {
        "name" : "Nikhil",
        "pass" : "linkin",
        "balance" : 50000
    }
}

def debit(acc_no):
    amt = int(input("Enter amount to debit: "))
    if data[acc_no]['balance'] < amt:
        print("Not Enough Amount")
        return
    else:
        data[acc_no]['balance'] = data[acc_no]['balance'] - amt

def credit(acc_no):
    amt = int(input("Enter amount to debit: "))
    data[acc_no]['balance'] = data[acc_no]['balance'] + amt
    print("Amount added to account")

def balance_enquiry(acc_no):
    print("Balance : ", data[acc_no]['balance'])

def update_record(acc_no):
    password = getpass("Enter new Password: ")
    con_password = getpass("Confirm new Password: ")
    if password != con_password:
        print("Password Doesn't match!! Please Enter again")
        return True
    data[acc_no]['pass'] = password
    return False

def Bank(acc_no):
    choice = int(input("""Enter what to do
1. Debit
2. Credit
3. Balance Enquiry
4. Update Record
5. Logout\n"""))
    if choice == 1:
        debit(acc_no)
        return True
    elif choice == 2:
        credit(acc_no)
        return True
    elif choice == 3:
        balance_enquiry(acc_no)
        return True
    elif choice == 4:
        x = True
        while x == True:
            x = update_record(acc_no)
        return True
    else:
        return False

def login():
    acc_name = int(input("Enter account number: "))
    if acc_name not in data:
        print("Data Not available")
        return
    password = getpass("Password: ")
    if data[acc_name]['pass'] != password:
        print("Invalid Crediantials!!! Try again")
        return
    x = True
    while x == True:    
        x = Bank(acc_name)

def signup():
    acc_name = int(input("Enter account number: "))
    if acc_name in data:
        print("Account Number already exist")
        return
    name = input("Enter Name: ")
    password = getpass("Password: ")
    amt = 0
    data[acc_name] = {}
    data[acc_name][template[0]] = name
    data[acc_name][template[1]] = password
    data[acc_name][template[2]] = amt

def start():
    print("Welcome to Bank Services".center(100))
    x = int(input("1. Login\n2. Signup\n3. Exit\n"))
    if x == 1:
        login()
    elif x == 2:
        signup()
    else:
        exit()

if __name__ == '__main__':
    x = True
    while x == True:
        start()
        x = bool(input("Enter do you want to continue. (True/ False): ").capitalize())