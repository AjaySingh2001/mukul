import os
import json
import datetime


class ToDo:
    file_path = '/home/developer/Mukul/to_do_list/tasks.json'
        
    def due_date(self):
        day = int(input("Enter the day: "))
        month = int(input("Enter the month: "))
        year = int(input("Enter the year: "))
        x = datetime.datetime(year, month, day)

        return x.strftime("%x")
    
    
    def read_tasks(self):
        tasks = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                tasks = json.load(file)
        else:
            print("*******************")
        return tasks
    
    
    def write_task(self, tasks):
        with open(self.file_path, 'w') as file:
            json.dump(tasks, file, indent=4)
            
            
    # Add a new task
    def view_all_task(self):
        tasks = self.read_tasks()
        print(" id | description | status | due_date " )
        for i in tasks:
            if i['status']:
                print(f"{i['id']} | {i['description']} | Done! | {i['due_date']}")
            else:
                print(f"{i['id']} | {i['description']} | Pending | {i['due_date']}")
                
    
    # View all tasks
    def add_task(self,desc):
        if not os.path.exists(self.file_path) or os.stat(self.file_path).st_size == 0:
            new_task = [{
                "id": 1,
                "description": desc,
                "status": False,
                "due_date":self.due_date()
            }]
            self.write_task(new_task)
            print(f"Created new file and added {desc}")
            return

        tasks = self.read_tasks()

        # For Unique Id
        if len(tasks) == 0:
            new_id = 1
        else:
            new_id = tasks[-1]['id'] + 1
        
        new_task = {
                "id": new_id,
                "description": desc,
                "status": False,
                "due_date": self.due_date()
        }
        
        tasks.append(new_task)
        self.write_task(tasks)
        
        print("Congratulation you have successfully added a task!!")
    
    
    # Mark a task as done
    def check_task(self):
        tasks = self.read_tasks()
        self.view_all_task()
        id = int(input("Mark a task which you have done :"))
        for i in tasks:          
            if i['id'] == id:
                i["status"] = True
                break
        else:
            print("Please enter a valid id!!")
        self.write_task(tasks)
        
        print("Congratulation you have completed a task id - {id}")
        self.view_all_task()
        
        return 

    # Delete a task
    def delete_task(self):
        tasks = self.read_tasks()
        self.view_all_task()
        
        id = int(input("Enter the id for deleting a task: "))
        ind = -1
        for i in tasks:
            if i['id'] == id:
                ind = tasks.index(i)
                print("Removed task is: ",tasks.pop(ind))
                break
            
        self.write_task(tasks)
        
        self.read_tasks()
        return 
        
    # modifying description of task
    def modify_task(self):
        tasks = self.read_tasks()
        self.view_all_task()
        
        id = int(input("Enter the id for modifying description: "))
        text = input("Enter the new text: ")
        for i in tasks:
            if i['id'] == id:
                i['description'] = text
                break
        
        self.write_task(tasks)
        self.view_all_task()
        



if __name__ == "__main__":
    
    task = ToDo()
    while True:
        
        print("\t\t\t\t\t\tWelcome to To Do List")
        print('1. Add a new task\n2. View all tasks\n3. Mark a task as done\n4. Delete a task\n5. Modify Task \n6. Exit')
        operation = input("\nEnter Operation Number:")
        
        if operation == 1:
            description = input("Enter the Task: ").strip()
            task.add_task(description)
            
        elif operation == 2:
            task.view_all_task()
            
        elif operation == 3:
            task.check_task()
            
        elif operation == 4:
            task.delete_task()
        
        elif operation == 5:
            task.modify_task()
            
        elif operation == 6:
            exit()
        else:
            print("\nWrong Input Please Enter Correct Input.")