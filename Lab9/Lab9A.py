#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab9A

def all_math(input1, input2):
    result = [input1 + input2, input1 - input2, input1 * input2, input1 / input2 if input2 != 0 else None,
              input1 // input2 if input2 != 0 else None, input1 % input2 if input2 != 0 else None, input1 ** input2]
    return result



def main():
    input1 = int(input("Enter your first number: "))
    input2 = int(input("Enter your second number: "))
    print(f"Your resulting tuple is {all_math(input1, input2)}")

if __name__ == "__main__":
    main()