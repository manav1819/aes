def string_to_matrix(hex_string):
    """
    Converts a 32-hexits string into a 4x4 matrix, filled column-wise.
    
    Args:
        hex_string (str): A string of 32 hexadecimal characters.
        
    Returns:
        list: A 4x4 matrix where each element is 2 hexits.
    """
    if len(hex_string) != 32:
        raise ValueError("Input string must be exactly 32 hex characters long.")
    
    # Create an empty 4x4 matrix
    matrix = [['' for _ in range(4)] for _ in range(4)]
    
    # Fill the matrix column-wise
    for col in range(4):
        for row in range(4):
            matrix[row][col] = hex_string[(col * 4 + row) * 2: (col * 4 + row + 1) * 2]
    
    return matrix
