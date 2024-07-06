import streamlit as st

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A')) if encrypt else chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        elif 'a' <= char <= 'z':
            result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a')) if encrypt else chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
        else:
            result += char
    return result

def main():
    st.title("Caesar Cipher Encryption and Decryption")

    action = st.sidebar.radio("Select Action", ["Encrypt", "Decrypt"])

    message = st.text_area("Enter a message:")

    shift = st.number_input("Enter the shift value:", min_value=0, step=1)

    if action == "Encrypt":
        result = caesar_cipher(message, shift, encrypt=True)
        st.text("Encrypted message:")
        st.text(result)
    elif action == "Decrypt":
        result = caesar_cipher(message, shift, encrypt=False)
        st.text("Decrypted message:")
        st.text(result)

if __name__ == "__main__":
    main()
