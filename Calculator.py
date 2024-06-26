def calculator_app():
    while True:
        try:
            print("Select operation:")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")

            choice = input("Enter choice(1/2/3/4): ")

            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(num1, "+", num2, "=", num1 + num2)

                elif choice == '2':
                    print(num1, "-", num2, "=", num1 - num2)

                elif choice == '3':
                    print(num1, "*", num2, "=", num1 * num2)

                elif choice == '4':
                    if num2!= 0:
                        print(num1, "/", num2, "=", num1 / num2)
                    else:
                        print("Error! Division by zero is not allowed.")
            else:
                print("Invalid input")

            try_again = input("Do you want to try again? (yes/no): ")
            if try_again.lower()!= "yes":
                print("Thank you!")
                break

        except ValueError:
            print("Error! Invalid input. Please enter a number.")

if __name__ == "__main__":
    calculator_app()