# >= 75 — Distinction
# >= 60 — First Class
# >= 50— Second Class
# <= 50— Fail
def grade(Data):
    Sum = 0
    per = 0.0
    for no in Data:
        Sum = Sum + no
    per = (Sum / 600) * 100 
    return per
        

def main():
    Marks = list()
    print("_"*30)
    print("Enter all six subjects marks")
    print("_"*30)

    print("")
    no = int(input("1. Enter the marks of Marathi : "))
    Marks.append(no)

    no = int(input("2. Enter the marks of Hindi : "))
    Marks.append(no)

    no = int(input("3. Enter the marks of English : "))
    Marks.append(no)

    no = int(input("4. Enter the marks of Mathematics : "))
    Marks.append(no)

    no = int(input("5. Enter the marks of Science : "))
    Marks.append(no)

    no = int(input("6. Enter the marks of Social Science : "))
    Marks.append(no)

    Ret = grade(Marks)

    print("_"*35)

    if (Ret >= 75):
        print(f"Your socre is {Ret:.2f}% Distinction")
    elif (Ret >=60 and Ret <= 75):
        print(f"Your score is {Ret:.2f}% First Class")
    elif (Ret >= 50 and Ret <=60):
        print(f"Your score is {Ret:.2f}% Second Class")
    elif ( Ret < 50):
        print(f"Your score is {Ret:.2f}% Fail")
    print("_"*35)

if __name__ == "__main__":
    main()