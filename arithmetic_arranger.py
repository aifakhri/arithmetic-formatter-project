def arithmetic_arranger(problems: list, result=False) -> str:
    """
    Parsing arithmetic operations in a list. Only accepts + and - operation.
    Calculate the arithmetic problems if required.

    Parameters:
    -----------
    problems : list
        list of arithmetic problems
    result : bool
        deciding whether the result is displayed or not

    Returns
    -------
    str
        The text of the arithmetic calculation
    """

    # Setup empty lists
    first_operands = list()
    second_operands = list()
    dashes = list()
    outputs = list()

    # Return Error if it is more than 5
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Iterate through the problems
    for problem in problems:
        # splitting problems in the list
        fs_operand, operator, sc_operand = problem.split()
        if fs_operand.strip().isdigit == False \
            or sc_operand.strip().isdigit() == False:
            return "Error: Numbers must only contain digits."
        elif len(fs_operand) > 4 or len(sc_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Checking arithmetic operation
        if operator == "+":
            output = str(int(fs_operand) + int(sc_operand))
        elif operator == "-":
            output = str(int(fs_operand) - int(sc_operand))
        else:
            return "Error: Operator must be '+' or '-'."

        # Arranging second operator
        operator = operator + " "
        if len(fs_operand) > len(sc_operand):
            sc_operand = operator + sc_operand.rjust(len(fs_operand))
        else:
            sc_operand = operator + sc_operand

        # Arranging first operator
        fs_operand = fs_operand.rjust(len(sc_operand))
        dash = "-"*len(sc_operand)
        output = output.rjust(len(sc_operand))

        # Append manipulation to the list before
        first_operands.append(fs_operand)
        second_operands.append(sc_operand)
        dashes.append(dash)
        outputs.append(output)

    # Joining the operation strings
    first_string = "    ".join(first_operands).rstrip()
    second_string = "    ".join(second_operands).rstrip()
    third_string = "    ".join(dashes).rstrip()
    last_string = "    ".join(outputs).rstrip()

    # Deciding whether result should be displayed or not
    if result == False:
        arranged_problems = first_string + "\n" + second_string \
                            + '\n' + third_string
    else:
        arranged_problems = first_string + '\n' + second_string \
                            + '\n' + third_string + '\n' + last_string

    return arranged_problems


if __name__ == "__main__":
    pass
