def arithmetic_arranger(problems, result=False):
    first_operands = list()
    second_operands = list()
    dashes = list()
    outputs = list()
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for problem in problems:
        fs_operand, operator, sc_operand = problem.split()

    if fs_operand.strip().isdigit == False or sc_operand.strip().isdigit() == False:
        return 'Error: Numbers must only contain digits.'
    elif len(fs_operand) > 4 or len(sc_operand) > 4:
        return 'Error: Numbers cannot be more than four digits.'

    if operator == '+':
        output = str(int(fs_operand) + int(sc_operand))
    elif operator == '-':
        output = str(int(fs_operand) - int(sc_operand))
    else:
        return "Error: Operator must be '+' or '-'."

    operator = operator + " "
    if len(fs_operand) > len(sc_operand):
        sc_operand = operator + sc_operand.rjust(len(fs_operand))
    else:
        sc_operand = operator + sc_operand

    fs_operand = fs_operand.rjust(len(sc_operand))
    dash = '-'*len(sc_operand)
    output = output.rjust(len(sc_operand))

    first_operands.append(fs_operand)
    second_operands.append(sc_operand)
    dashes.append(dash)
    outputs.append(output)

    first_string = '    '.join(first_operands).rstrip()
    second_string = '    '.join(second_operands).rstrip()
    third_string = '    '.join(dashes).rstrip()
    last_string = '    '.join(outputs).rstrip()

    if result == False:
        arranged_problems = first_string + '\n' + second_string + '\n' + third_string
    else:
        arranged_problems = first_string + '\n' + second_string + '\n' + third_string + '\n' + last_string

    return arranged_problems


if __name__ == "__main__":
    print(arithmetic_arranger(["32 + 698"]))
