import time
import streamlit as st
import streamlit.components.v1 as components
def Caesar_Cipher(inp,val):
    enstr = ""
    for i in inp:
        if 'A' <= i <= 'Z':
            enstr += chr(((ord(i) - ord('A') + val) % 26) + ord('A'))
        elif 'a' <= i <= 'z':
            enstr += chr(((ord(i) - ord('a') + val) % 26) + ord('a'))
        else:
            enstr += i
    return enstr
def User_Interface(str1, str2):
    with st.spinner(text="Please Wait", cache=True):
        time.sleep(2)
    with st.status(f"{str1} data"):
        time.sleep(2)
        st.write(f"{str2} done")
    pg = st.progress(0)
    for i in range(101):
        pg.progress(i)
        time.sleep(0.01)
    st.success(f"{str2} done :smiley:")
flag=0
components.html('''<style> body{padding:20px;}</style><body bgcolor = "powderblue"><h1><center><b>Caesar Cipher</h1></body>''')
st1 = st.file_uploader("Click here to upload file",type="txt")
if st1 is not None:
    f_open = st1.read()
    f_open = f_open.decode('utf-8')
    inp = f_open
if st1 is None:
   st.markdown("### OR")
   st.subheader("Enter the text")
   inp = st.text_input("Text")
opt = st.selectbox("Select the operation",("Encrypt","Decrypt"))

if opt == "Decrypt":
    val1= st.selectbox("Choose the value to decrypt",(-1,-2,-3,-4,-5))
    btn = st.button("Click to decrypt")
    if btn == True:
       flag = 1
elif opt== "Encrypt":
     val = st.selectbox("Choose the Value to Encrypt",(1,2,3,4,5))
     btn = st.button("Click to Encrypt")
     if btn == True:
        flag =2
if  flag== 2:
    User_Interface("Encrypting","Encryption")
    res = Caesar_Cipher(inp,val)
    st.code(res)
    st.download_button(label="Download Encrypted File :open_file_folder:",data=res,file_name="Encrypted.txt", help="Click to download")
elif flag==1:
     User_Interface("Decrypting","Decryption")
     res = Caesar_Cipher(inp,val1)
     st.code(res)
     st.download_button(label="Download Decrypted File :open_file_folder:", data=res, file_name="Decrypted.txt",help="Click to download")
