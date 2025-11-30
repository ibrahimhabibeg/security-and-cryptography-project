from .utils import char_to_idx, idx_to_char

def vignere_encrypt(text, key):
    text = ''.join([c for c in text.lower() if c.isalpha()])
    key = key * (len(text) // len(key)) + key[: (len(text) % len(key))]
    key = [char_to_idx(c) for c in key]
    text = [char_to_idx(c) for c in text]
    res = []
    for x, k in zip(text, key):
        res.append((x + k) % 26)
    return "".join([idx_to_char(i) for i in res])

def vignere_decrypt(text, key):
    text = ''.join([c for c in text.lower() if c.isalpha()])
    key = key * (len(text) // len(key)) + key[: (len(text) % len(key))]
    key = [char_to_idx(c) for c in key]
    text = [char_to_idx(c) for c in text]
    res = []
    for x, k in zip(text, key):
        res.append((x - k) % 26)
    return "".join([idx_to_char(i) for i in res])