def char_to_idx(c):
    return ord(c.lower()) - ord('a')

def idx_to_char(i):
    return chr(i + ord('a'))