def rail_fence_encrypt(text, rails):
    text = ''.join([c for c in text if c.isalpha()])
    cipher = []
    for i in range(rails):
        cipher.append("")
    row = 0
    direction = 1
    for char in text:
        cipher[row] += char

        if row == rails - 1:
            direction = -1
        elif row == 0:
            direction = 1
        row += direction
    return ''.join(cipher)

def rail_fence_decrypt(ciphertext, rails):
    ciphertext = ''.join([c for c in ciphertext if c.isalpha()])
    row_sizes = [0] * rails
    row = 0
    direction = 1
    for _ in ciphertext:
        row_sizes[row] += 1
        if row == rails - 1:
            direction = -1
        elif row == 0:
            direction = 1
        row += direction
    rows = []
    start = 0
    for size in row_sizes:
        rows.append(ciphertext[start:start + size])
        start += size
    plaintext = ""
    row = 0
    direction = 1
    for _ in ciphertext:
        plaintext += rows[row][0]
        rows[row] = rows[row][1:]
        if row == rails - 1:
            direction = -1
        elif row == 0:
            direction = 1
        row += direction
    return plaintext