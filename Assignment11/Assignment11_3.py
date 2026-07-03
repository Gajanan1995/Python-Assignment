def DigitsSum(No):
    Count = 0
    while(No != 0):
        Count += No % 10                # Extracts or get the last digit (e.g., 4)
        No = No // 10                   # Removes the last digit (e.g., 123)
    return Count 
        
def main():
    print("Enter the Number : ")    
    no = int(input())                   # 1234
    Result = DigitsSum(no)

    print("Summation is :",Result)      # 10

if __name__ == "__main__":
    main()