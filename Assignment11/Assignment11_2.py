def DigCount(No):
    Count = 0
    while(No != 0):
        No = No // 10
        print(No)
        Count = Count + 1 
    return Count 
        
def main():
    print("Enter the number : ")
    no = int(input())

    Ret = DigCount(no)
    print("Number of Digits is : ",Ret)

if __name__ == "__main__":
    main()