def add_task():
    task = input("kaam likho:")
    with open("my_tasks.txt", "a")as file:
        file.write(task + "\n")
    print("save ho gaya!")

def show_tasks():
    try:
        with open("my_tasks.txt", "r")as file:
            print("\n---Tumhari List---")
            print(file.read())
    except:
        print("Abhi koi kaam nahi hai")

while True:
    print("\n1.kaam add karo  2. kaam dekho  3. exit")
    ch = input("kya karna hai?")

    if ch == '1': add_task()
    elif ch == '2': show_tasks()
    elif ch == '3': break                
