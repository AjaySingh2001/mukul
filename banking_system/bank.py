import os

class Account:
    
    file_path = '/home/developer/Mukul/banking_system/accounts.txt'
    
    def read_accounts(self):
        accounts = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
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
        
        with open(self.file_path, 'w') as file:
            for acc in accounts:
                acc_name = acc['holder_name'].strip()
                line = (f"{acc['acc_no']}, {acc_name}, {acc['balance']}, {acc['active']}\n")
                file.write(line)
        return
        
    
    def deposit(self, acc_no, amount):

        accounts = self.read_accounts()
        for acc in accounts:

            if int(acc['acc_no']) == int(acc_no):
                acc['balance'] = float(acc['balance']) + amount
                break
            
        self.create_account(accounts)
        
        
        
    def withdraw(self, acc_no, amount):
        accounts = self.read_accounts()
        for acc in accounts:
            
            if int(acc['acc_no']) == acc_no and float(acc['balance']) >= amount:
                acc['balance'] = float(acc['balance']) - amount
                print(f"Successfully Withdraw an amount of {amount}")
                self.create_account(accounts)
                return True
        return False
            
        
        
        
    def get_balance(self, acc_no):
        accounts = self.read_accounts()
        for acc in accounts:
            
            if int(acc['acc_no']) == acc_no:
                return float(acc['balance'])
    
    
    def __str__(self):
        return f"Account holder name: {self.name} and account no: {self.account_no} ."


class Bank:
    def __init__(self, name, acc_list):
        self.name = name
        self.account_list = acc_list
        
        
    def add_account(self):
        name = input("Enter the name: ")
        new_acc = Account()
        accounts = new_acc.read_accounts()
        acc_no = 1
        if len(accounts) > 0:
            acc_no = int(accounts[-1]["acc_no"]) + 1
        
        accounts.append({'acc_no': acc_no, 'holder_name': name, 'balance': 0, 'active': 1}) 
        
        new_acc.create_account(accounts)
        (self.account_list).append(new_acc)
        print("Successfully added a new account..")
        # number = (acc['acc_no']).strip()
        # name = (acc['holder_name']).strip()
        # balance = (acc['balance']).strip()
        print(f"\t\t\t\t\t\tAccount no: {acc_no}\n\t\t\t\t\t\tName: {name}\n\t\t\t\t\t\tBalance: 0")
    
    
    
    def find_account(self, acc_no):
        
        temp = Account()
        accounts = temp.read_accounts()
        
        for acc in accounts:
        
            if int(acc['acc_no']) == acc_no:
                print("account found successfully!!")
                number = (acc['acc_no']).strip()
                name = (acc['holder_name']).strip()
                balance = (acc['balance']).strip()
                print(f"\t\t\t\t\t\tAccount no: {number}\n\t\t\t\t\t\tName: {name}\n\t\t\t\t\t\tBalance: {balance}")
                return acc
        else:
            print("Account not found..")
            return None
    
    
    
    def deposit_to_account(self, acc_no, amount):
        
        obj = Account()
        temp = self.find_account(acc_no)
        if temp:
            obj.deposit(int(temp['acc_no']), amount)
            return
    
    
    
    def withdraw_from_account(self, acc_no, amount):
        
        temp = Account()
        temp.withdraw(acc_no, amount)

    
    def check_balance(self, acc_no):
        temp = Account()
        print("Your Current Balance is: ", temp.get_balance(acc_no))
            
            
            
    def transfer(self, from_acc, to_acc, amount):
        acc1 = self.find_account(from_acc)
        acc2 = self.find_account(to_acc)
        if acc1 and acc2:
            temp = Account()
            if temp.withdraw(int(acc1['acc_no']), amount):
                temp.deposit(int(acc2['acc_no']), amount)
                print(f"Amount {amount} Successfully transferred from {from_acc} to {to_acc}")
            else:
                print("Not Enough Money..")
        elif not acc1:
            print("Account does not exist for sending money.")
        elif not acc2:
            print("Account does not exist for sending money.")
        
        
        
    def close_account(self, acc_no):
        temp = Account()
        accounts = temp.read_accounts()
        for acc in accounts:
            if int(acc['acc_no']) == acc_no:
                if bool(int(acc['active'])):
                    acc['active'] = False
                else:
                    acc['active'] = True

    
    
    def __str__(self):
        return f"Bank Name: {self.name}"


def check(amount):
    if amount > 0:
        return True
    else:
        print("Please Enter the correct amount...")
        return False

if __name__ == "__main__":
    
    print("\t\t\t\t\t Welcome to bestpeers bank")
    
    bank1 = Bank('SBI', [])
    

    while True:
        print('1. Add new account.\n2. Find Account.\n3. Deposit Amount.\n4. Withdraw Amount.\n5. Check Balance\n6. Transfer money\n7. Close Account\n8. Exit')
        op = input("enter operation no: ")
        if op == '' or op not in ['1','2','3','4','5','6','7','8']:
            print("Please Enter proper operation.")
            continue
        else:
            op = int(op)
        
        if op == 1:
            bank1.add_account()
            
        elif op == 2:
            acc_no = int(input("Enter Account No: "))
            bank1.find_account(acc_no)
        
        elif op == 3:
            acc_no = int(input("Enter Account No: "))
            amount = float(input("Enter the amount: "))
            if check(amount):
                bank1.deposit_to_account(acc_no, amount)
                
            
        elif op == 4:
            acc_no = int(input("Enter Account No: "))
            amount = float(input("Enter the amount: "))
            if check(amount):
                bank1.withdraw_from_account(acc_no, amount)
            
        elif op == 5:
            acc_no = int(input("Enter Account No: "))
            bank1.check_balance(acc_no)
            
        elif op == 6:
            from_acc = float(input("Enter the account number from where to you have send money: "))
            amount = float(input("Enter the amount: "))
            if not check(amount):
                continue
            to_acc = float(input("Enter the account number where you have to send: "))
            bank1.transfer(from_acc, to_acc, amount)
        
        elif op == 7:
            acc_no = int(input("Enter Account No: "))
            bank1.close_account(acc_no)
            
        elif op == 8:
            exit()
        else:
            print("Please enter correct input operation.")
    
        
    