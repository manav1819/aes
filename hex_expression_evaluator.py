from poly_addition import xor_hex_mod_11b
from poly_multiplication import gf2_multiply_and_mod
import re


def evaluate_expression(expression):
    """
    Evaluate a string expression containing hexadecimal numbers and operators
    (+ for addition and * for multiplication) using BODMAS rules.

    Args:
        expression (str): The string expression to evaluate.

    Returns:
        str: The result of the evaluation in hexadecimal format.
    """

    def tokenize(expr):
        """
        Tokenize the input string into hex numbers and operators.

        Args:
            expr (str): The input string.

        Returns:
            list: A list of tokens (hex numbers and operators).
        """
        tokens = re.findall(r'[0-9A-Fa-f]{2}|\+|\*|\(|\)|\{|\}|\[|\]', expr)
        return tokens

    def evaluate_simple_expression(tokens):
        """
        Evaluate a flat list of tokens (no parentheses).

        Args:
            tokens (list): List of tokens.

        Returns:
            str: The result of the evaluation.
        """
        # Handle multiplication (*) first
        while '*' in tokens:
            index = tokens.index('*')
            # Multiply the two operands around the '*'
            product = gf2_multiply_and_mod(tokens[index - 1], tokens[index + 1])
            # Replace the operation with the result
            tokens = tokens[:index - 1] + [product] + tokens[index + 2:]

        # Handle addition (+)
        result = tokens[0]
        for i in range(1, len(tokens), 2):
            result = xor_hex_mod_11b(result, tokens[i + 1])
        return result

    def evaluate_with_parentheses(tokens, open_bracket, close_bracket):
        """
        Evaluate tokens containing specific brackets.

        Args:
            tokens (list): List of tokens.
            open_bracket (str): Opening bracket.
            close_bracket (str): Closing bracket.

        Returns:
            list: The updated list of tokens.
        """
        while open_bracket in tokens:
            # Find the innermost bracket
            start = len(tokens) - tokens[::-1].index(open_bracket) - 1
            end = tokens.index(close_bracket, start)
            if end == -1:
                raise ValueError(f"Unmatched {open_bracket} in expression.")
            # Evaluate the content inside the brackets
            inner_result = evaluate_simple_expression(tokens[start + 1:end])
            # Replace the bracketed content with its result
            tokens = tokens[:start] + [inner_result] + tokens[end + 1:]
        return tokens

    # Step 1: Remove spaces
    expression = re.sub(r'\s+', '', expression)

    # Step 2: Tokenize the expression
    tokens = tokenize(expression)

    # Step 3: Evaluate parentheses in order of priority
    tokens = evaluate_with_parentheses(tokens, '(', ')')  # Round brackets
    tokens = evaluate_with_parentheses(tokens, '[', ']')  # Square brackets
    tokens = evaluate_with_parentheses(tokens, '{', '}')  # Curly braces

    # Step 4: Evaluate the final simple expression
    return evaluate_simple_expression(tokens)


# Example usage
if __name__ == "__main__":
    user_expression = input("Enter a string expression (e.g., '00 + 01 * 03'): ")
    try:
        result = evaluate_expression(user_expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
