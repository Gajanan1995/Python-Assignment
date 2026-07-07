def Div(No):

    if(No % 5 == 0):
        return True
    else:
        return False
    
def main():
    print("Enter the Number ")
    no = int(input())

    Ans = Div(no)
    print(Ans)
if __name__ == "__main__":
    main()