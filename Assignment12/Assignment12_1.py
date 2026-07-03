def VowelOrConsonant(data):
    if data.lower() in {'a', 'e', 'i', 'o','u'}:
        return True
    else:
        return False
def main():

    char = ''

    while True:
        char = input("Enter a single character: ")
        if len(char) == 1 and char.isalpha():
            break
        else:
            print("Please Enter a single character to continue: ")

    Ret = VowelOrConsonant(char)

    if Ret:
        print(f"{char}, is Vowel")
    else:
        print(f"{char}, is Consonant")

if __name__ == "__main__":
    main()