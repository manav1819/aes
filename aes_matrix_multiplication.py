from poly_addition import xor_hex_mod_11b
from poly_multiplication import gf2_multiply_and_mod

matrix_a = [
        ['0E', '0B', '0D', '09'],
        ['09', '0E', '0B', '0D'],
        ['0D', '09', '0E', '0B'],
        ['0B', '0D', '09', '0E']
    ]

    # Default matrix_b
matrix_b = [
        ['02', '03', '01', '01'],
        ['01', '02', '03', '01'],
        ['01', '01', '02', '03'],
        ['03', '01', '01', '02']
    ]

def matrix_multiply_mod_11b_decrypt(matrix_a, user_matrix):
    """
    Perform matrix multiplication in GF(2^8) with reduction modulo 0x11B for decryption.

    Args:
        matrix_a (list): Left matrix (hexadecimal strings).
        user_matrix (list): Custom right matrix (hexadecimal strings) provided by the user.

    Returns:
        list: Resultant matrix after multiplication.
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(user_matrix[0])

    # Initialize the result matrix
    result = [['00' for _ in range(cols_b)] for _ in range(rows_a)]

    # Perform matrix multiplication
    for i in range(rows_a):
        for j in range(cols_b):
            element_sum = '00'  # Start with 0 in hex
            for k in range(cols_a):
                # Multiply and XOR the values
                product = gf2_multiply_and_mod(matrix_a[i][k], user_matrix[k][j])
                element_sum = xor_hex_mod_11b(element_sum, product)
            result[i][j] = element_sum

    return result


def matrix_multiply_mod_11b_encrypt(matrix_b, user_matrix):
    """
    Perform matrix multiplication in GF(2^8) with reduction modulo 0x11B for encryption.

    Args:
        matrix_b (list): Left matrix (hexadecimal strings).
        user_matrix (list): Custom right matrix (hexadecimal strings) provided by the user.

    Returns:
        list: Resultant matrix after multiplication.
    """
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
    cols_user = len(user_matrix[0])

    # Initialize the result matrix
    result = [['00' for _ in range(cols_user)] for _ in range(rows_b)]

    # Perform matrix multiplication
    for i in range(rows_b):
        for j in range(cols_user):
            element_sum = '00'  # Start with 0 in hex
            for k in range(cols_b):
                # Multiply and XOR the values
                product = gf2_multiply_and_mod(matrix_b[i][k], user_matrix[k][j])
                element_sum = xor_hex_mod_11b(element_sum, product)
            result[i][j] = element_sum

    return result


