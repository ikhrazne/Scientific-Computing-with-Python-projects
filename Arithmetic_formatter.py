

def arithmetic_arranger(problems, solved=False):
    first_line_components = []
    second_line_components = []
    third_line_components = []
    fourth_line_components = []

    # too many problem
    if len(problems) >= 5:
        return "Error: Too many problems"

    for problem in problems:
        operator = problem.split(" ")[1]
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'"

        try:
            a = problem.split(" ")[0]
            b = problem.split(" ")[2]
        except Exception:
            return "Error: Numbers must only contain digits"

        if len(a) > 4 or len(b) > 4:
            return "Error: Numbers cannot be more than four digits"

        result = str(eval(problem))
        max_length_of_numbers = max(len(a), len(b), len(result))

        first_line_components.append((max_length_of_numbers - len(a) + 2) * " " + a)
        second_line_components.append(operator + (max_length_of_numbers - len(b) + 1) * " " + b)
        third_line_components.append((max_length_of_numbers + 2) * "-")
        fourth_line_components.append((max_length_of_numbers - len(a) + 2) * " " + result)

    print("    ".join(first_line_components))
    print("    ".join(second_line_components))
    print("    ".join(third_line_components))

    if solved:
        print("    ".join(fourth_line_components))


if __name__ == "__main__":
    final_result = arithmetic_arranger(["12 * 5", "15 + 5"])

    if type(final_result) == str:
        print(final_result)
