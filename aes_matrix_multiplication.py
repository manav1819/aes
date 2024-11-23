from poly_addition import xor_hex_mod_11b
from poly_multiplication import gf2_multiply_and_mod

# Define the matrices in hexadecimal
matrix_a = [
    ['0E', '0B', '0D', '09'],
    ['09', '0E', '0B', '0D'],
    ['0D', '09', '0E', '0B'],
    ['0B', '0D', '09', '0E']
]

matrix_b = [
    ['A1', 'B3', 'B4', '59'],
    ['4B', '97', '26', '11'],
    ['03', '48', 'C8', 'A1'],
    ['9F', 'CC', '5F', '9F']
]

def matrix_multiply_mod_11b(matrix_a, matrix_b):
    """
    Perform matrix multiplication in GF(2^8) with reduction modulo 0x11B.
    
    Args:
        matrix_a (list): Left matrix (hexadecimal strings).
        matrix_b (list): Right matrix (hexadecimal strings).
        
    Returns:
        list: Resultant matrix after multiplication.
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    # Initialize the result matrix
    result = [['00' for _ in range(cols_b)] for _ in range(rows_a)]

    # Perform matrix multiplication
    for i in range(rows_a):
        for j in range(cols_b):
            element_sum = '00'  # Start with 0 in hex
            for k in range(cols_a):
                # Multiply and XOR the values
                product = gf2_multiply_and_mod(matrix_a[i][k], matrix_b[k][j])
                element_sum = xor_hex_mod_11b(element_sum, product)
            result[i][j] = element_sum

    return result

# Perform the matrix multiplication
result_matrix = matrix_multiply_mod_11b(matrix_a, matrix_b)

# Print the final result
for row in result_matrix:
    print(row)
