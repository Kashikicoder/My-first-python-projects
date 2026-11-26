marks =int(input("Apna marks daalo(0-100): "))

if marks >= 0 and marks <= 100:
    if marks >= 90:
        print("Grade: A+, Tu Topper hai!")
        if marks == 100:
            print("Arre Waah! Full Marks! Scholarship pakki!")
    elif marks >= 75:
            print("Grade: A, Bahut Badhiya!")
    elif marks >= 60:
            print("Grade: B, Thoda Aur Mehant Karo!")
    elif marks >= 33:
            print("Grade: C, pass ho gaya!")
    else:
            print("Grade: F, Fail ho gaya!")
else:
        print("Galat Marks Daale hai!")
