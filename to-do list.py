todo = []

print("Welcome to my To-Do List!")

while True:
    print("\n1. Kaam Add Karo")
    print("2. List Dekho")
    print("3. Kaam Delete Karo")
    print("4. Bahar Niklo")

    choice = input("Apna option likho (1-4): ")

    if choice == "1":
        kaam = input("Kya kaam karna hai? ")
        todo.append(kaam)
        print("Add ho gaya!")

    elif choice == "2":
        print("\n--- Teri List ---")
        if len(todo) == 0:
            print("List khaali hai!")
        else:
            for i in range(len(todo)):
                print(f"{i+1}. {todo[i]}")

    elif choice == "3":
        num = int(input("Konsa number delete karna hai? "))
        todo.pop(num-1)
        print("Delete ho gya!")

    elif choice == "4":
        print("Bye Bye!")
        break

    else:
        print("Galat option!")