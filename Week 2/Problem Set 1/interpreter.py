def separate_expression(expr):
    expr = expr.split(" ")
    if len(expr) == 1:
        return expr[0]
    else:
        return expr

def evaluate_expression(expr):
    try:
        firstNum = float(expr[0])
        operator = expr[1]
        secondNum = float(expr[2])
    except ValueError:
        raise ValueError("Invalid numbers in expression.")

    match operator:
        case '+':
            return firstNum + secondNum
        case '-':
            return firstNum - secondNum
        case '*':
            return firstNum * secondNum
        case '/':
            return firstNum / secondNum
        case '%':
            return firstNum % secondNum

def main():
    expression = input("Enter a mathematical expression: ").strip().lower()
    print(evaluate_expression(separate_expression(expression)))

if __name__ == "__main__":
    main()
