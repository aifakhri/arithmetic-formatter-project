import os
from arithmetic_arranger import arithmetic_arranger


CLEAR_COMMAND = "cls" if os.name == "nt" else "clear"
VALUE_ERROR_MSG = "Please enter string"


def number_entry_menu(num: int):
    counter = 0
    operations = []
    for i in range(num):
        print(
             "============================================\n"
            f" Problem {i+1}: Enter the desired numbers   \n"
             "============================================\n"
        )
        try:
            f_operand = int(input("Enter the First Operand [Integer]: "))
            s_operand = int(input("Enter the Second Operand [Integer]: "))
            operator = input("Enter Arithmetic Operator [+ or -]: ")
            operator = operator.strip(" ")
            if ("+" in operator) or ("-" in operator):
                operation = f"{f_operand} {operator} {s_operand}"
                operations.append(operation)
                os.system(CLEAR_COMMAND)
            else:
                counter += 1
                os.system(CLEAR_COMMAND)
        except ValueError:
            print(VALUE_ERROR_MSG)
            os.system(CLEAR_COMMAND)
            counter += 1
    
    if counter == 0:
        print("Calculation result\n")
        print(arithmetic_arranger(operations, True))
    else:
        print("\nYou have input error, please enter the correct input\n")

def main():
    while True:
        print("=============================================\n"
              "   Welcome to simple Arithmetic Formatter    \n"
              "=============================================\n"
              "1. Enter Arithmetic Problem\n"
              "2. Exit Program\n")

        try:
            choice = int(input("Enter Menu [1-2]: "))
            if choice == 1:
                n_calc = int(input("How Many Calculation [1-5]? "))
                if n_calc > 5 or n_calc <= 0:                
                    print(f"You can't do {n_calc} calculation " 
                        "Maximum Calculation is 5\n")
                else:
                    os.system(CLEAR_COMMAND)
                    number_entry_menu(n_calc)
            elif choice == 2:
                exit()
            else:
                print("Menu is not available")
                os.system(CLEAR_COMMAND)
            input("Please Press Enter to Continue")
            os.system(CLEAR_COMMAND)
        except ValueError:
            print(VALUE_ERROR_MSG)
            input("Please Press Enter to Continue")
            os.system(CLEAR_COMMAND)

main()