from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operation")
    num1 = float(input("Enter First Number?"))
    num2 = float(input("Enter Second Number?"))
    operation = input("Enter the operation (add, subtract, multiply, divide):")
    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}" )  
if __name__=="__main__":
    main()
