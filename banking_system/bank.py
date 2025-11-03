import os

# class Account
class Account:
    FILE_PATH = '/home/developer/Mukul/banking_system/accounts.txt'
    
    def read_accounts(self):
        accounts = []
        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        acc_no, name, __balance, active = parts
                        accounts.append({"acc_no": acc_no,
                                    "holder_name": name, 
                                    "balance": __balance, 
                                    "active": active
                                    })        
        return accounts
    
    
    def create_account(self, accounts :list):
        with open(self.FILE_PATH, 'w') as file:
            for acc in accounts:
                acc_no = acc['acc_no'].strip()
                acc_name = acc['holder_name'].strip()
                balance = acc['balance']
                active = acc['active']
                line = (f"{acc_no}, {acc_name}, {balance}, {active}\n")
                file.write(line)
        return
        
    
    def deposit(self, acc_no, amount):
        accounts = self.read_accounts()
        for acc in accounts:
            if acc['acc_no'] == acc_no:
                acc['balance'] = float(acc['balance']) + amount
                break  
        self.create_account(accounts)
        
        
    def withdraw(self, acc_no, amount):
        accounts = self.read_accounts()
        for acc in accounts:
            if acc['acc_no'] == acc_no:
                if float(acc['balance']) >= amount:
                    acc['balance'] = float(acc['balance']) - amount
                    self.create_account(accounts)
                else:
                    print("You do not have sufficiant amount.")
                    return False
        return True
            
        
    def get_balance(self, acc_no):
        accounts = self.read_accounts()
        for acc in accounts:
            if acc['acc_no'] == acc_no:
                return float(acc['balance'])
    
    
    def account_status(self, acc_no):
        accounts = self.read_accounts()
        for acc in accounts:
            if acc['acc_no'] == acc_no:
                s = acc['active'].strip()
                val = int(s)
                if val == 1:
                    return True 
        return False
            
            
    def __str__(self):
        return f"Account holder name: {self.name} and account no: {self.account_no} ."


# class Bank
class Bank:
    def __init__(self, name, acc_list):
        self.name = name
        self.account_list = acc_list
        
        
    def add_account(self):
        name = input("Enter the name: ")
        new_acc = Account()
        accounts = new_acc.read_accounts()
        acc_no = '00000000000001'
        if len(accounts) > 0:
            acc_no = int(accounts[-1]["acc_no"]) + 1
            s = str(acc_no)
            while len(s) != 14:
                s = '0'+s
            acc_no = s
        new_data = {'acc_no': acc_no, 'holder_name': name, 'balance': 0, 'active': 1}
        accounts.append(new_data)         
        new_acc.create_account(accounts)
        (self.account_list).append(new_acc)        
        return new_data
    
    
    def find_account(self, acc_no):        
        temp = Account()
        accounts = temp.read_accounts()        
        for acc in accounts:
            if acc['acc_no'] == acc_no:                
                return acc        
        return None
    
    
    def deposit_to_account(self, acc_no, amount):        
        obj = Account()
        temp = self.find_account(acc_no)
        if temp:
            obj.deposit(temp['acc_no'], amount)
            return
    
    
    def withdraw_from_account(self, acc_no, amount):      
        temp = Account()
        return temp.withdraw(acc_no, amount)

    
    def check_balance(self, acc_no):
        temp = Account()
        return temp.get_balance(acc_no)
            
            
    def transfer(self, from_acc, to_acc, amount):
        acc1 = self.find_account(from_acc)
        acc2 = self.find_account(to_acc)
        if acc1 and acc2:
            temp = Account()
            if temp.withdraw(acc1['acc_no'], amount):
                temp.deposit(acc2['acc_no'], amount)
                return True            
        elif not acc1:
            print("Account does not exist for sending money.")
        elif not acc2:
            print("Account does not exist for sending money.")        
        return False

        
    def close_account(self, acc_no):
        temp = Account()
        accounts = temp.read_accounts()
        for acc in accounts:
            if acc['acc_no'] == acc_no:
                if temp.account_status(acc_no):
                    acc['active'] = '0'
                    print(f"Account no {acc['acc_no']}, {acc['holder_name']} has been disabled.")
                    break
                else:
                    acc['active'] = '1'
                    print(f"Account no {acc['acc_no']}, {acc['holder_name']} has been activated.")
                    break        
        temp.create_account(accounts)

    
    def __str__(self):
        return f"Bank Name: {self.name}"


# User Class
class User(Account, Bank):
    
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        
        
# User Seperate operations
def menu(acc):    
    print("Successfully added a new account..")
    user = User(acc['acc_no'], acc['holder_name'], acc['balance'])
    while True:
        os.system('clear')
        print("\t\t\t\t\tWelcome to bestpeers bank")
        print(f"\t\t\t\t\tWelcome to the bank !! {acc['holder_name']} !!")
        print(f"\nAccount Details here...\nAccount no: {user.acc_no}\nName: {user.name}\nBalance: {user.check_balance(user.acc_no)}\n")
        print('1. Deposit Amount.\n2. Withdraw Amount.\n3. Transfer money.\n4. Main menu ')
        op = input("enter operation no: ")
        if op == '' or op not in ['1','2','3','4']:
            print("Please Enter proper operation.")
            continue
        else:
            op = int(op)
            if op == 1:
                amount = float(input("Enter the amount: "))
                if check(amount):
                    user.deposit_to_account(user.acc_no, amount)
                    print(f"Congratulation!! you have successfully added {amount} Rupees in your account. ")
                    
            elif op == 2:
                amount = float(input("Enter the amount: "))
                if check(amount):
                    user.withdraw_from_account(user.acc_no, amount)
                    print(f"You have successfully withdraw {amount} to your account.")
            
            elif op == 3:
                amount = float(input("Enter the amount: "))
                if not check(amount):
                    continue
                to_acc = input("Enter the account number where you have to send: ")
                
                if not user.account_status(to_acc):
                    print("Account Does not exists.")
                    continue
                if user.transfer(user.acc_no, to_acc, amount):
                    print(f"Successfully transferred amount {amount} to {to_acc}")
                    
            elif op == 4:
                print(f"Bye....!! Thank you {user.name} for using BestPeers Bank!!!")
                return
        b = input("Please enter for continue.")

 
def check(amount):
    if amount > 0:
        return True
    else:
        print("Please Enter the correct amount...")
        return False


if __name__ == "__main__":
    bank1 = Bank('SBI', [])
    account1 = Account()
    while True:
        os.system('clear')
        print("\t\t\t\t\tWelcome to bestpeers bank")
        print("\t\t\t\t\tWelcome to the bank !! Manager!!")
        print('1. Add new account.\n2. Find Account.\n3. Deposit Amount.\n4. Withdraw Amount.\n5. Check Balance\n6. Transfer money\n7. Close/Active Account\n8. Exit')
        op = input("enter operation no: ")
        if op == '' or op not in ['1','2','3','4','5','6','7','8']:
            print("Please Enter proper operation.")
            continue
        else:
            op = int(op)    
                
        if op == 1:
            acc = bank1.add_account()
            menu(acc)
            b = input("Press Enter for back.")
            continue      
              
        elif op == 2:
            acc_no = input("Enter Account No: ")
            acc = bank1.find_account(acc_no)
            if not acc:
                print("account not found!!")
            else:
                print("account found successfully!!")
                print(f"\n\t\t\t\t\t\tAccount no: {(acc['acc_no']).strip()}\n\t\t\t\t\t\tName: {(acc['holder_name']).strip()}\n\t\t\t\t\t\tBalance: {(acc['balance']).strip()}\n")
                            
        elif op == 3:
            acc_no = input("Enter Account No: ")
            if not account1.account_status(acc_no):
                print("Account Does not exists.")
                continue
            amount = float(input("Enter the amount: "))
            if check(amount):
                bank1.deposit_to_account(acc_no, amount)
            print(f"Manager has successfully added {amount} Rupees in account {acc_no}. ")
                
        elif op == 4:
            acc_no = input("Enter Account No: ")
            if not account1.account_status(acc_no):
                print("Account Does not exists.")
                continue
            amount = float(input("Enter the amount: "))
            if check(amount):
                if bank1.withdraw_from_account(acc_no, amount):                
                    print(f"Manager successfully Withdraw an amount of {amount} from {acc_no}.")
            
        elif op == 5:
            acc_no = input("Enter Account No: ")
            if not account1.account_status(acc_no):
                print("Account Does not exists.")
                continue
            acc = bank1.find_account(acc_no)
            print(f"\n\t\t\t\t\t\tAccount no: {(acc['acc_no']).strip()}\n\t\t\t\t\t\tName: {(acc['holder_name']).strip()}\n\t\t\t\t\t\tBalance: {(acc['balance']).strip()}\n")
            blank = input("Please enter for continue.")
            
        elif op == 6:
            from_acc = input("Enter the account number from where to you have send money: ")
            if not account1.account_status(from_acc):
                print("Account Does not exists.")
                continue
            amount = float(input("Enter the amount: "))
            if not check(amount):
                continue
            to_acc = input("Enter the account number where you have to send: ")
            
            if not account1.account_status(to_acc):
                print("Account Does not exists.")
                continue
            if bank1.transfer(from_acc, to_acc, amount):
                print(f"Manager transfered {amount} from {from_acc} to {to_acc}.")
        
        elif op == 7:
            acc_no = input("Enter Account No: ")
            bank1.close_account(acc_no)
            
        elif op == 8:
            exit()
            
        else:
            print("Please enter correct input operation.")        
        b = input("Please enter for continue.")
    
        
    