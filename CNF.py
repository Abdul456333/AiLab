import sympy.logic.boolalg as boolalg
from sympy import symbols

def convert_to_cnf(expression):
    """
    Converts a logical expression to Conjunctive Normal Form (CNF)
    """
    # Parse the expression into a SymPy Boolean expression
    expr = boolalg.to_cnf(expression, True)
    return expr

def get_input():
    """
    Takes user input for a logical expression
    """
    print("Enter the logical expression in terms of AND, OR, and NOT.")
    print("Use & for AND, | for OR, and ~ for NOT.")
    print("Example: (A & B) | ~C")
    
    user_input = input("Enter expression: ")
    
    # Define symbols (you can expand this list based on user input)
    A, B, C, D = symbols('A B C D')
    
    # Replace input variables with actual symbols
    user_input = user_input.replace('A', 'A').replace('B', 'B').replace('C', 'C').replace('D', 'D')
    
    # Convert input to a Boolean expression
    try:
        expression = boolalg.sympify(user_input)
        return expression
    except Exception as e:
        print("Error in input expression:", e)
        return None

def main():
    expression = get_input()
    
    if expression:
        print("\nOriginal Expression:", expression)
        cnf_expression = convert_to_cnf(expression)
        print("Converted CNF Expression:", cnf_expression)

if __name__ == "__main__":
    main()
