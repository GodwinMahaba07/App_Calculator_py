#pseudocode

#user input choice of operation
def calculator_app():
    while True:
        try:
            print("Select operation:")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")

            choice = input("Enter choice(1/2/3/4): ")

# input two numbers from the user
# perform the chosen operation
# add "do you want to try again"