def circular_permute_matrix_decryption(matrix):
    """
    Circularly permute the elements of each row in the matrix based on hardcoded decryption shifts.

    Decryption Shifts:
    Row 0: Shift right by 1
    Row 1: Shift right by 4
    Row 2: Shift right by 3
    Row 3: Shift right by 2

    Args:
        matrix (list): A 2D list representing the matrix.
        
    Returns:
        list: The matrix with rows circularly shifted for decryption.
    """
    # Hardcoded shifts for decryption
    shifts = [0, 1, 2, 3]
    
    permuted_matrix = []

    # Apply circular shift for each row
    for row, shift in zip(matrix, shifts):
        shift %= len(row)  # Ensure the shift doesn't exceed the row length
        permuted_row = row[-shift:] + row[:-shift]  # Circularly shift right
        permuted_matrix.append(permuted_row)

    return permuted_matrix


def circular_permute_matrix_encryption(matrix):
    """
    Circularly permute the elements of each row in the matrix based on hardcoded encryption shifts.

    Encryption Shifts:
    Row 0: Shift left by 1
    Row 1: Shift left by 2
    Row 2: Shift left by 3
    Row 3: Shift left by 4

    Args:
        matrix (list): A 2D list representing the matrix.
        
    Returns:
        list: The matrix with rows circularly shifted for encryption.
    """
    # Hardcoded shifts for encryption
    shifts = [0, 1, 2, 3]
    
    permuted_matrix = []

    # Apply circular shift for each row
    for row, shift in zip(matrix, shifts):
        shift %= len(row)  # Ensure the shift doesn't exceed the row length
        permuted_row = row[shift:] + row[:shift]  # Circularly shift left
        permuted_matrix.append(permuted_row)

    return permuted_matrix
