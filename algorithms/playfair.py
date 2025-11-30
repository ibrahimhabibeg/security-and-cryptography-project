from .utils import char_to_idx, idx_to_char

def create_playfair_matrix(key):
    matrix = [[-1 for _ in range(5)] for _ in range(5)]
    j_idx = char_to_idx('j')
    used = [False]*26
    matrix_idx = 0
    for c in key.lower():
        idx = char_to_idx(c)
        if idx == j_idx:
            idx = char_to_idx('i')   
        if not used[idx] and c.isalpha():
            used[idx] = True
            matrix[matrix_idx // 5][matrix_idx % 5] = idx
            matrix_idx += 1
    for i in range(26):
        if i == j_idx:
            continue
        if not used[i]:
            used[i] = True
            matrix[matrix_idx // 5][matrix_idx % 5] = i
            matrix_idx += 1
    return matrix

def get_position(matrix, char):
    idx = char_to_idx(char)
    if idx == char_to_idx('j'):
        idx = char_to_idx('i')
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == idx:
                return (i, j)
    return None

def playfair_encrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    
    plaintext = plaintext.lower().replace("j", "i")
    plaintext = ''.join([c for c in plaintext if c.isalpha()])
    
    digraphs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        if i + 1 < len(plaintext):
            b = plaintext[i + 1]
            if a == b:
                digraphs.append((a, 'x'))
                i += 1
            else:
                digraphs.append((a, b))
                i += 2
        else:
            digraphs.append((a, 'x'))
            i += 1
            
    ciphertext = ""
    for a, b in digraphs:
        row_a, col_a = get_position(matrix, a)
        row_b, col_b = get_position(matrix, b)
        
        if row_a == row_b:
            ciphertext += idx_to_char(matrix[row_a][(col_a + 1) % 5])
            ciphertext += idx_to_char(matrix[row_b][(col_b + 1) % 5])
        elif col_a == col_b:
            ciphertext += idx_to_char(matrix[(row_a + 1) % 5][col_a])
            ciphertext += idx_to_char(matrix[(row_b + 1) % 5][col_b])
        else:
            ciphertext += idx_to_char(matrix[row_a][col_b])
            ciphertext += idx_to_char(matrix[row_b][col_a])
    return ciphertext.upper()

def clean_deciphered(deciphered):
    cleaned = ''
    i = 0
    while i < len(deciphered):
        if i < len(deciphered) - 2 and i > 0 and deciphered[i] == 'x' and deciphered[i-1] == deciphered[i+1]:
            i += 1
        else:
            cleaned += deciphered[i]
            i += 1
    if cleaned[-1] == 'x':
        cleaned = cleaned[:-1]
    return cleaned

def playfair_decrypt(ciphertext, key):
    matrix = create_playfair_matrix(key)
    
    ciphertext = ''.join([c for c in ciphertext.lower() if c.isalpha()])
    
    digraphs = []
    i = 0
    while i < len(ciphertext):
        a = ciphertext[i]
        b = ciphertext[i + 1]
        digraphs.append((a, b))
        i += 2
            
    plaintext = ""
    for a, b in digraphs:
        row_a, col_a = get_position(matrix, a)
        row_b, col_b = get_position(matrix, b)
        
        if row_a == row_b:
            plaintext += idx_to_char(matrix[row_a][(col_a - 1) % 5])
            plaintext += idx_to_char(matrix[row_b][(col_b - 1) % 5])
        elif col_a == col_b:
            plaintext += idx_to_char(matrix[(row_a - 1) % 5][col_a])
            plaintext += idx_to_char(matrix[(row_b - 1) % 5][col_b])
        else:
            plaintext += idx_to_char(matrix[row_a][col_b])
            plaintext += idx_to_char(matrix[row_b][col_a])
    
    return clean_deciphered(plaintext)