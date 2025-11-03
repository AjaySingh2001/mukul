import json
from datetime import datetime
import os

class LMS:
    
    file_path = '/home/developer/Mukul/LMS/books.txt'
    
    def read_books(self)->list:
        books = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        id, title, author, avail = parts
                        books.append({"id": id,
                                    "title": title, 
                                    "author": author, 
                                    "available_books": avail
                                    })        
        return books
    
    
    def write_book(self, books :list):
        
        with open(self.file_path, 'w') as file:
            for b in books:
                tit = b['title'].strip()
                auth = b['author'].strip()
                line = (f"{b['id']}, {tit}, {auth}, {b['available_books']}\n")
                file.write(line)
        return
        
        
    # Add Book to library
    def add_book(self, title, author):

        books = self.read_books()
        id = 1
        if len(books) > 0:
            id = int(books[-1]["id"]) + 1
        
        for i in books:
            if i['title'].strip() == title and i['author'].strip() == author:
                i['available_books'] = int(i['available_books']) + 1
                break
        else:
            books.append({'id': id, 'title': title, 'author': author, 'available_books': 1})     

        self.write_book(books)
        print("Congratulation!! you have successfully added a book !!!")
        return 
        

            
    # Check available books
    def available_book(self):  
        data = self.read_books()
        print("Book Id | Book Name | Book Author | Available Book \n")
        for i in data:
            id, title, auth, avail = i['id'].strip(), i['title'].strip(), i['author'].strip(), i['available_books'].strip()
            print(f"{id} | {title} | {auth} | {avail}")
            print()
            
            
    # Borrow book from library        
    def borrow_book(self):
        self.available_book()
        b_id = int(input("Enter Id for borrowing book: "))
        data = self.read_books()
            
        for i in data:
            if int(i['id']) == b_id:
                if int(i['available_books']) > 0:
                    i['available_books'] = int(i['available_books']) - 1
                    print("Congratulation you have successfully borrow book -", i['title'] , "at", datetime.now())
                    break
                else:
                    print("Sorry!! Book is not Available at this time...")
                    
        self.write_book(data)
                
                
    # Return book 
    def return_book(self, book_id):
        data = self.read_books()
            
        for i in data:
            if int(i['id']) == book_id:
                i['available_books'] = int(i['available_books']) + 1
                print("Congratulation you have successfully return book", "at", datetime.now())
                break
                    
        self.write_book(data)
        



if __name__ == "__main__":
    
    lib = LMS()
    while True:
        
        print("\t\t\t\t\t\tWelcome to Library")
        print('1. Add new books.\n2. Borrow books.\n3. Return books.\n4. View available books.\n5. Exit')
        operation = input("\nEnter Operation Number:")
        
        if operation == 1:
            title = input("Enter the book title: ").strip()
            author = input("Enter author name: ").strip()
            lib.add_book(title, author)
            
        elif operation == 2:
            lib.borrow_book()
            
        elif operation == 3:
            book_id = int(input("Enter book id: "))
            lib.return_book(book_id)
            
        elif operation == 4:
            lib.available_book()
            
        elif operation == 5:
            exit()
        else:
            print("\nWrong Input Please Enter Correct Input.")
        