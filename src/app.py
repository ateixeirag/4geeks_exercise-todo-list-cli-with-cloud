import json, requests
todos = []

url='https://assets.breatheco.de/apis/fake/todos/user/'
user='lgallardo'
header={'Content-Type':'application/json'}

def get_todos():
    global todos
    return todos

def add_one_task(title):
    global todos
    data={'label': title, 'done': False}
    todos.append(data)

def print_list():
    global todos
    k=1
    for data in todos:
        print(k,data)
        k=k+1
    print()
    print(json.dumps(todos))
    print()

def delete_task(number_to_delete):
    global todos
    number_to_delete=int(number_to_delete)-1
    todos.pop(number_to_delete)
    print_list()

def initialize_todos():
    data=[]
    global todos
    r = requests.get(url+user)
    if(r.status_code == 404):
        print("No previous todos found, starting a new todolist")
        r = requests.post(url+user,headers=header,data=json.dumps(data)) 
        if r.status_code == 200:
            print("Tasks initialized successfully")
    else:
        print("A todo list was found, loading the todos...")
        todos = r.json()
    print()
    print(todos)
    
def save_todos():
    test=json.dumps(todos)
    print(test)
    r = requests.put(url+user,headers=header,data=json.dumps(todos))
    print(r.text)
    print(r.status_code)

def load_todos():
    r = requests.get(url+user)
    print(r.status_code)
    todos = r.json()
    print(todos)
    
    pass
    
if __name__ == '__main__':
    stop = False
    print("Initializing todos with previous data or creating a new todo's list...")
    initialize_todos()
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks3
        4. Send/Save todo's to API
        5. Retrieve todo's from API
        6. Exit
    """)
        response = input(' **** ==> ')
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            number_to_delete = input("What task number you want to delete? ")
            delete_task(number_to_delete)
        elif response == "1":
            title = input("What is your task title? ")
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")