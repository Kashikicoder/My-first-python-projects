print("---Calculator---")
print("1. Add (+)")
print("2. Minus (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Apna option chuno (1/2/3/4): ")

num1 = float(input("Pehla number daalo: "))
num2 = float(input("Dusra number daalo "))

if choice == '1':
    print("Result:", num1 + num2)
elif choice =='2':
    print("Result:", num1 - num2)
elif choice == '3':
    print("Result:", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("0 se divide nahi hoga !")
else:
    print("Galat option chuna!")       