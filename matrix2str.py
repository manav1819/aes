def matrix_to_string(matrix):
    """
    Converts a 4x4 matrix into a 32-hexits string, read column-wise.
    
    Args:
        matrix (list): A 4x4 matrix where each element is 2 hexits.
        
    Returns:
        str: A string of 32 hexadecimal characters.
    """
    if len(matrix) != 4 or any(len(row) != 4 for row in matrix):
        raise ValueError("Input must be a 4x4 matrix.")
    
    # Read the matrix column-wise to form the string
    hex_string = ""
    for col in range(4):
        for row in range(4):
            hex_string += matrix[row][col]
    
    return hex_string