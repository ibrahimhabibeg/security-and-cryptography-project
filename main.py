import streamlit as st
from algorithms.caesar import caesar_encrypt, caesar_decrypt
from algorithms.playfair import playfair_encrypt, playfair_decrypt
from algorithms.vigenere import vignere_encrypt, vignere_decrypt
from algorithms.autokey import autokey_encrypt, autokey_decrypt
from algorithms.rail_fence import rail_fence_encrypt, rail_fence_decrypt
from algorithms.des import des_encrypt, des_decrypt

st.title("Security and Cryptography Course Final Project")

st.header("Project Overview")
st.write("""
         This is the submission for the final project for the Security and Cryptography course (CSC 302; 2025-2026) at
         [Suez Canal University](https://suez.edu.eg/ar/en/) made by Ibrahim Habib.
         
        This projects implements multiple encryption and decryption algorithms discussed during the course. The algorithms
        included are:
        - Caesar Cipher
        - Playfair Cipher
        - Vigenere Cipher
        - AutoKey Cipher
        - Rail Fence Cipher
        - DES (Data Encryption Standard)
""")

st.header("Algorithms")

caesar_tab, playfair_tab, vigenere_tab, autokey_tab, railfence_tab, des_tab = st.tabs(
    [
        "Caesar Cipher",
        "Playfair Cipher",
        "Vigenere Cipher",
        "AutoKey Cipher",
        "Rail Fence Cipher",
        "DES",
    ]
)

st.session_state.setdefault("caesar_encrypt_plaintext", "meet me after the toga party")
st.session_state.setdefault("caesar_encrypt_key", 3)
st.session_state.setdefault("caesar_encrypt_ciphertext", "")
st.session_state.setdefault("caesar_decrypt_ciphertext", "")
st.session_state.setdefault("caesar_decrypt_key", 3)
st.session_state.setdefault("caesar_decrypt_plaintext", "")

with caesar_tab:
    st.subheader("Caesar Cipher Encryption")
    caesar_plaintext = st.text_area(
        "Enter plaintext for Caesar Cipher encryption:",
        value=st.session_state.caesar_encrypt_plaintext,
    )
    caesar_key = st.number_input(
        "Enter key (shift value) for Caesar Cipher:",
        min_value=1,
        max_value=25,
        value=st.session_state.caesar_encrypt_key,
    )
    st.caption("Note: The key should be an integer between 1 and 25.")
    st.write("Ciphertext")
    ciphertext_display = st.code(
        st.session_state.caesar_encrypt_ciphertext, language="text"
    )

    def encrypt_caesar():
        caesar_ciphertext = caesar_encrypt(caesar_plaintext, caesar_key)
        st.session_state.caesar_encrypt_plaintext = caesar_plaintext
        st.session_state.caesar_encrypt_key = caesar_key
        st.session_state.caesar_encrypt_ciphertext = caesar_ciphertext

    def copy_to_decrypt():
        st.session_state.caesar_decrypt_ciphertext = (
            st.session_state.caesar_encrypt_ciphertext
        )
        st.session_state.caesar_decrypt_key = st.session_state.caesar_encrypt_key

    buttons_container = st.container(horizontal=True, horizontal_alignment="distribute")
    with buttons_container:
        caesar_encrypt_button = st.button(
            "Encrypt with Caesar Cipher",
            type="primary",
            on_click=encrypt_caesar,
            key="caesar_encrypt",
        )
        caesar_copy_button = st.button(
            "Copy to Decrypt", on_click=copy_to_decrypt, key="caesar_copy_to_decrypt"
        )

    st.subheader("Caesar Cipher Decryption")
    caesar_ciphertext_input = st.text_area(
        "Enter ciphertext for Caesar Cipher decryption:",
        value=st.session_state.caesar_decrypt_ciphertext,
    )
    caesar_decrypt_key = st.number_input(
        "Enter key (shift value) for Caesar Cipher decryption:",
        min_value=1,
        max_value=25,
        value=st.session_state.caesar_decrypt_key,
    )
    st.caption("Note: The key should be an integer between 1 and 25.")
    st.write("Decrypted Plaintext")
    decrypted_plaintext_display = st.code(
        st.session_state.caesar_decrypt_plaintext, language="text"
    )

    def decrypt_caesar():
        decrypted_plaintext = caesar_decrypt(
            caesar_ciphertext_input, caesar_decrypt_key
        )
        st.session_state.caesar_decrypt_ciphertext = caesar_ciphertext_input
        st.session_state.caesar_decrypt_key = caesar_decrypt_key
        st.session_state.caesar_decrypt_plaintext = decrypted_plaintext

    def copy_to_encrypt():
        st.session_state.caesar_encrypt_plaintext = (
            st.session_state.caesar_decrypt_plaintext
        )
        st.session_state.caesar_encrypt_key = st.session_state.caesar_decrypt_key

    buttons_container_decrypt = st.container(
        horizontal=True, horizontal_alignment="distribute"
    )
    with buttons_container_decrypt:
        caesar_decrypt_button = st.button(
            "Decrypt with Caesar Cipher",
            type="primary",
            on_click=decrypt_caesar,
            key="caesar_decrypt",
        )
        caesar_copy_button_decrypt = st.button(
            "Copy to Encrypt", on_click=copy_to_encrypt, key="caesar_copy_to_encrypt"
        )


st.session_state.setdefault("playfair_encrypt_plaintext", "balloon")
st.session_state.setdefault("playfair_encrypt_key", "monarchy")
st.session_state.setdefault("playfair_encrypt_ciphertext", "")
st.session_state.setdefault("playfair_decrypt_ciphertext", "")
st.session_state.setdefault("playfair_decrypt_key", "")
st.session_state.setdefault("playfair_decrypt_plaintext", "")

with playfair_tab:
    st.subheader("Playfair Cipher Encryption")
    playfair_plaintext = st.text_area(
        "Enter plaintext for Playfair Cipher encryption:",
        value=st.session_state.playfair_encrypt_plaintext,
    )
    playfair_key = st.text_input(
        "Enter key for Playfair Cipher:", value=st.session_state.playfair_encrypt_key
    )
    st.write("Ciphertext")
    playfair_ciphertext_display = st.code(
        st.session_state.playfair_encrypt_ciphertext, language="text"
    )

    def encrypt_playfair():
        playfair_ciphertext = playfair_encrypt(playfair_plaintext, playfair_key)
        st.session_state.playfair_encrypt_plaintext = playfair_plaintext
        st.session_state.playfair_encrypt_key = playfair_key
        st.session_state.playfair_encrypt_ciphertext = playfair_ciphertext

    def copy_to_decrypt_playfair():
        st.session_state.playfair_decrypt_ciphertext = (
            st.session_state.playfair_encrypt_ciphertext
        )
        st.session_state.playfair_decrypt_key = st.session_state.playfair_encrypt_key

    buttons_container_playfair = st.container(
        horizontal=True, horizontal_alignment="distribute"
    )
    with buttons_container_playfair:
        playfair_encrypt_button = st.button(
            "Encrypt with Playfair Cipher",
            type="primary",
            on_click=encrypt_playfair,
            key="playfair_encrypt",
        )
        playfair_copy_button = st.button(
            "Copy to Decrypt",
            on_click=copy_to_decrypt_playfair,
            key="playfair_copy_to_decrypt",
        )

    st.subheader("Playfair Cipher Decryption")
    playfair_ciphertext_input = st.text_area(
        "Enter ciphertext for Playfair Cipher decryption:",
        value=st.session_state.playfair_decrypt_ciphertext,
    )
    playfair_decrypt_key = st.text_input(
        "Enter key for Playfair Cipher decryption:",
        value=st.session_state.playfair_decrypt_key,
    )
    st.write("Decrypted Plaintext")
    decrypted_playfair_plaintext_display = st.code(
        st.session_state.playfair_decrypt_plaintext, language="text"
    )

    def decrypt_playfair():
        decrypted_plaintext = playfair_decrypt(
            playfair_ciphertext_input, playfair_decrypt_key
        )
        st.session_state.playfair_decrypt_ciphertext = playfair_ciphertext_input
        st.session_state.playfair_decrypt_key = playfair_decrypt_key
        st.session_state.playfair_decrypt_plaintext = decrypted_plaintext

    def copy_to_encrypt_playfair():
        st.session_state.playfair_encrypt_plaintext = (
            st.session_state.playfair_decrypt_plaintext
        )
        st.session_state.playfair_encrypt_key = st.session_state.playfair_decrypt_key

    buttons_container_decrypt_playfair = st.container(
        horizontal=True, horizontal_alignment="distribute"
    )
    with buttons_container_decrypt_playfair:
        playfair_decrypt_button = st.button(
            "Decrypt with Playfair Cipher",
            type="primary",
            on_click=decrypt_playfair,
            key="playfair_decrypt",
        )
        playfair_copy_button_decrypt = st.button(
            "Copy to Encrypt",
            on_click=copy_to_encrypt_playfair,
            key="playfair_copy_to_encrypt",
        )

st.session_state.setdefault("vigenere_encrypt_plaintext", "wearediscoveredsaveyourself")
st.session_state.setdefault("vigenere_encrypt_key", "deceptive")
st.session_state.setdefault("vigenere_encrypt_ciphertext", "")
st.session_state.setdefault("vigenere_decrypt_ciphertext", "")
st.session_state.setdefault("vigenere_decrypt_key", "deceptive")
st.session_state.setdefault("vigenere_decrypt_plaintext", "")

with vigenere_tab:
    st.subheader("Vigenere Cipher Encryption")
    vigenere_plaintext = st.text_area(
        "Enter plaintext for Vigenere Cipher encryption:",
        value=st.session_state.vigenere_encrypt_plaintext,
    )
    vigenere_key = st.text_input(
        "Enter key for Vigenere Cipher:", value=st.session_state.vigenere_encrypt_key
    )
    st.write("Ciphertext")
    vigenere_ciphertext_display = st.code(
        st.session_state.vigenere_encrypt_ciphertext, language="text"
    )

    def encrypt_vigenere():
        vigenere_ciphertext = vignere_encrypt(vigenere_plaintext, vigenere_key)
        st.session_state.vigenere_encrypt_plaintext = vigenere_plaintext
        st.session_state.vigenere_encrypt_key = vigenere_key
        st.session_state.vigenere_encrypt_ciphertext = vigenere_ciphertext

    def copy_to_decrypt_vigenere():
        st.session_state.vigenere_decrypt_ciphertext = (
            st.session_state.vigenere_encrypt_ciphertext
        )
        st.session_state.vigenere_decrypt_key = st.session_state.vigenere_encrypt_key

    buttons_container_vigenere = st.container(
        horizontal=True, horizontal_alignment="distribute"
    )
    with buttons_container_vigenere:
        vigenere_encrypt_button = st.button(
            "Encrypt with Vigenere Cipher",
            type="primary",
            on_click=encrypt_vigenere,
            key="vigenere_encrypt",
        )
        vigenere_copy_button = st.button(
            "Copy to Decrypt",
            on_click=copy_to_decrypt_vigenere,
            key="vigenere_copy_to_decrypt",
        )
        
    st.subheader("Vigenere Cipher Decryption")
    vigenere_ciphertext_input = st.text_area(
        "Enter ciphertext for Vigenere Cipher decryption:",
        value=st.session_state.vigenere_decrypt_ciphertext,
    )
    vigenere_decrypt_key = st.text_input(
        "Enter key for Vigenere Cipher decryption:",
        value=st.session_state.vigenere_decrypt_key,
    )
    st.write("Decrypted Plaintext")
    decrypted_vigenere_plaintext_display = st.code(
        st.session_state.vigenere_decrypt_plaintext, language="text"
    )
    
    def decrypt_vigenere():
        decrypted_plaintext = vignere_decrypt(
            vigenere_ciphertext_input, vigenere_decrypt_key
        )
        st.session_state.vigenere_decrypt_ciphertext = vigenere_ciphertext_input
        st.session_state.vigenere_decrypt_key = vigenere_decrypt_key
        st.session_state.vigenere_decrypt_plaintext = decrypted_plaintext
    
    def copy_to_encrypt_vigenere():
        st.session_state.vigenere_encrypt_plaintext = (
            st.session_state.vigenere_decrypt_plaintext
        )
        st.session_state.vigenere_encrypt_key = st.session_state.vigenere_decrypt_key
        
    buttons_container_decrypt_vigenere = st.container(
        horizontal=True, horizontal_alignment="distribute"
    )
    with buttons_container_decrypt_vigenere:
        vigenere_decrypt_button = st.button(
            "Decrypt with Vigenere Cipher",
            type="primary",
            on_click=decrypt_vigenere,
            key="vigenere_decrypt",
        )
        vigenere_copy_button_decrypt = st.button(
            "Copy to Encrypt",
            on_click=copy_to_encrypt_vigenere,
            key="vigenere_copy_to_encrypt",
        )

st.session_state.setdefault("autokey_encrypt_plaintext", "wearediscoveredsaveyourself")
st.session_state.setdefault("autokey_encrypt_key", "deceptive")
st.session_state.setdefault("autokey_encrypt_ciphertext", "")
st.session_state.setdefault("autokey_decrypt_ciphertext", "")
st.session_state.setdefault("autokey_decrypt_key", "deceptive")
st.session_state.setdefault("autokey_decrypt_plaintext", "")

with autokey_tab:
    st.subheader("AutoKey Cipher Encryption")
    autokey_plaintext = st.text_area(
        "Enter plaintext for AutoKey Cipher encryption:",
        value=st.session_state.autokey_encrypt_plaintext,
    )
    autokey_key = st.text_input(
        "Enter key for AutoKey Cipher:", value=st.session_state.autokey_encrypt_key
    )
    st.write("Ciphertext")
    autokey_ciphertext_display = st.code(
        st.session_state.autokey_encrypt_ciphertext, language="text"
    )

    def encrypt_autokey():
        autokey_ciphertext = autokey_encrypt(autokey_plaintext, autokey_key)
        st.session_state.autokey_encrypt_plaintext = autokey_plaintext
        st.session_state.autokey_encrypt_key = autokey_key
        st.session_state.autokey_encrypt_ciphertext = autokey_ciphertext

    def copy_to_decrypt_autokey():
        st.session_state.autokey_decrypt_ciphertext = (
            st.session_state.autokey_encrypt_ciphertext
        )
        st.session_state.autokey_decrypt_key = st.session_state.autokey_encrypt_key

    buttons_container_autokey = st.container(
        horizontal=True, horizontal_alignment="distribute"
    )
    with buttons_container_autokey:
        autokey_encrypt_button = st.button(
            "Encrypt with AutoKey Cipher",
            type="primary",
            on_click=encrypt_autokey,
            key="autokey_encrypt",
        )
        autokey_copy_button = st.button(
            "Copy to Decrypt",
            on_click=copy_to_decrypt_autokey,
            key="autokey_copy_to_decrypt",
        )
        
    st.subheader("AutoKey Cipher Decryption")
    autokey_ciphertext_input = st.text_area(
        "Enter ciphertext for AutoKey Cipher decryption:",
        value=st.session_state.autokey_decrypt_ciphertext,
    )
    autokey_decrypt_key = st.text_input(
        "Enter key for AutoKey Cipher decryption:",
        value=st.session_state.autokey_decrypt_key,
    )
    st.write("Decrypted Plaintext")
    decrypted_autokey_plaintext_display = st.code(
        st.session_state.autokey_decrypt_plaintext, language="text"
    )
    
    def decrypt_autokey():
        decrypted_plaintext = autokey_decrypt(
            autokey_ciphertext_input, autokey_decrypt_key
        )
        st.session_state.autokey_decrypt_ciphertext = autokey_ciphertext_input
        st.session_state.autokey_decrypt_key = autokey_decrypt_key
        st.session_state.autokey_decrypt_plaintext = decrypted_plaintext
        
    def copy_to_encrypt_autokey():
        st.session_state.autokey_encrypt_plaintext = (
            st.session_state.autokey_decrypt_plaintext
        )
        st.session_state.autokey_encrypt_key = st.session_state.autokey_decrypt_key
        
    buttons_container_decrypt_autokey = st.container(
        horizontal=True, horizontal_alignment="distribute"
    )
    
    with buttons_container_decrypt_autokey:
        autokey_decrypt_button = st.button(
            "Decrypt with AutoKey Cipher",
            type="primary",
            on_click=decrypt_autokey,
            key="autokey_decrypt",
        )
        autokey_copy_button_decrypt = st.button(
            "Copy to Encrypt",
            on_click=copy_to_encrypt_autokey,
            key="autokey_copy_to_encrypt",
        )
        

st.session_state.setdefault("railfence_encrypt_plaintext", "meet me after party")
st.session_state.setdefault("railfence_encrypt_rails", 3)
st.session_state.setdefault("railfence_encrypt_ciphertext", "")
st.session_state.setdefault("railfence_decrypt_ciphertext", "")
st.session_state.setdefault("railfence_decrypt_rails", 3)
st.session_state.setdefault("railfence_decrypt_plaintext", "")

with railfence_tab:
    st.subheader("Rail Fence Cipher Encryption")
    railfence_plaintext = st.text_area(
        "Enter plaintext for Rail Fence Cipher encryption:",
        value=st.session_state.railfence_encrypt_plaintext,
    )
    railfence_rails = st.number_input(
        "Enter number of rails for Rail Fence Cipher:",
        min_value=2,
        value=st.session_state.railfence_encrypt_rails,
    )
    st.caption("Note: The number of rails should be at least 2.")
    st.write("Ciphertext")
    railfence_ciphertext_display = st.code(
        st.session_state.railfence_encrypt_ciphertext, language="text"
    )

    def encrypt_railfence():
        railfence_ciphertext = rail_fence_encrypt(
            railfence_plaintext, railfence_rails
        )
        st.session_state.railfence_encrypt_plaintext = railfence_plaintext
        st.session_state.railfence_encrypt_rails = railfence_rails
        st.session_state.railfence_encrypt_ciphertext = railfence_ciphertext
        
    def copy_to_decrypt_railfence():
        st.session_state.railfence_decrypt_ciphertext = (
            st.session_state.railfence_encrypt_ciphertext
        )
        st.session_state.railfence_decrypt_rails = st.session_state.railfence_encrypt_rails
        
    buttons_container_railfence = st.container(
        horizontal=True, horizontal_alignment="distribute"
    )
    with buttons_container_railfence:
        railfence_encrypt_button = st.button(
            "Encrypt with Rail Fence Cipher",
            type="primary",
            on_click=encrypt_railfence,
            key="railfence_encrypt",
        )
        railfence_copy_button = st.button(
            "Copy to Decrypt",
            on_click=copy_to_decrypt_railfence,
            key="railfence_copy_to_decrypt",
        )
        
    st.subheader("Rail Fence Cipher Decryption")
    railfence_ciphertext_input = st.text_area(
        "Enter ciphertext for Rail Fence Cipher decryption:",
        value=st.session_state.railfence_decrypt_ciphertext,
    )
    railfence_decrypt_rails = st.number_input(
        "Enter number of rails for Rail Fence Cipher decryption:",
        min_value=2,
        value=st.session_state.railfence_decrypt_rails,
    )
    st.caption("Note: The number of rails should be at least 2.")
    st.write("Decrypted Plaintext")
    decrypted_railfence_plaintext_display = st.code(
        st.session_state.railfence_decrypt_plaintext, language="text"
    )
    
    def decrypt_railfence():
        decrypted_plaintext = rail_fence_decrypt(
            railfence_ciphertext_input, railfence_decrypt_rails
        )
        st.session_state.railfence_decrypt_ciphertext = railfence_ciphertext_input
        st.session_state.railfence_decrypt_rails = railfence_decrypt_rails
        st.session_state.railfence_decrypt_plaintext = decrypted_plaintext
        
    def copy_to_encrypt_railfence():
        st.session_state.railfence_encrypt_plaintext = (
            st.session_state.railfence_decrypt_plaintext
        )
        st.session_state.railfence_encrypt_rails = st.session_state.railfence_decrypt_rails
        
    buttons_container_decrypt_railfence = st.container(
        horizontal=True, horizontal_alignment="distribute"
    )
    with buttons_container_decrypt_railfence:
        railfence_decrypt_button = st.button(
            "Decrypt with Rail Fence Cipher",
            type="primary",
            on_click=decrypt_railfence,
            key="railfence_decrypt",
        )
        railfence_copy_button_decrypt = st.button(
            "Copy to Encrypt",
            on_click=copy_to_encrypt_railfence,
            key="railfence_copy_to_encrypt",
        )
        
st.session_state.setdefault("des_encrypt_plaintext", "02468aceeca86420")
st.session_state.setdefault("des_encrypt_key", "0f1571c947d9e859")
st.session_state.setdefault("des_encrypt_ciphertext", "")
st.session_state.setdefault("des_decrypt_ciphertext", "")
st.session_state.setdefault("des_decrypt_key", "0f1571c947d9e859")
st.session_state.setdefault("des_decrypt_plaintext", "")

with des_tab:
    st.subheader("DES Encryption")
    des_plaintext = st.text_area(
        "Enter plaintext (in hex) for DES encryption:",
        value=st.session_state.des_encrypt_plaintext,
    )
    des_key = st.text_input(
        "Enter key (in hex) for DES:", value=st.session_state.des_encrypt_key
    )
    st.write("Ciphertext (in hex)")
    des_ciphertext_display = st.code(
        st.session_state.des_encrypt_ciphertext, language="text"
    )

    def encrypt_des():
        des_ciphertext = des_encrypt(des_plaintext, des_key)
        st.session_state.des_encrypt_plaintext = des_plaintext
        st.session_state.des_encrypt_key = des_key
        st.session_state.des_encrypt_ciphertext = des_ciphertext

    def copy_to_decrypt_des():
        st.session_state.des_decrypt_ciphertext = (
            st.session_state.des_encrypt_ciphertext
        )
        st.session_state.des_decrypt_key = st.session_state.des_encrypt_key

    buttons_container_des = st.container(
        horizontal=True, horizontal_alignment="distribute"
    )
    with buttons_container_des:
        des_encrypt_button = st.button(
            "Encrypt with DES",
            type="primary",
            on_click=encrypt_des,
            key="des_encrypt",
        )
        des_copy_button = st.button(
            "Copy to Decrypt",
            on_click=copy_to_decrypt_des,
            key="des_copy_to_decrypt",
        )
        
    st.subheader("DES Decryption")
    des_ciphertext = st.text_area(
        "Enter ciphertext (in hex) for DES decryption:",
        value=st.session_state.des_decrypt_ciphertext,
    )
    des_decrypt_key = st.text_input(
        "Enter key (in hex) for DES decryption:", value=st.session_state.des_decrypt_key
    )
    st.write("Plaintext (in hex)")
    des_plaintext_display = st.code(
        st.session_state.des_decrypt_plaintext, language="text"
    )

    def decrypt_des():
        des_plaintext = des_decrypt(des_ciphertext, des_decrypt_key)
        st.session_state.des_decrypt_ciphertext = des_ciphertext
        st.session_state.des_decrypt_key = des_decrypt_key
        st.session_state.des_decrypt_plaintext = des_plaintext

    def copy_to_encrypt_des():
        st.session_state.des_encrypt_plaintext = st.session_state.des_decrypt_plaintext
        st.session_state.des_encrypt_key = st.session_state.des_decrypt_key

    buttons_container_des_decrypt = st.container(
        horizontal=True, horizontal_alignment="distribute"
    )
    with buttons_container_des_decrypt:
        des_decrypt_button = st.button(
            "Decrypt with DES",
            type="primary",
            on_click=decrypt_des,
            key="des_decrypt",
        )
        des_copy_button_decrypt = st.button(
            "Copy to Encrypt",
            on_click=copy_to_encrypt_des,
            key="des_copy_to_encrypt",
        )
        
st.header("Acknowledgements")
st.write("""
         I would like to thank both
         - **Dr. Osama Helmy**: For his lectures and guidance throughout the course.
         - **Dr. Yasmin El-Leithy**: For her hands-on classes and sessions.
""")