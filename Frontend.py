import streamlit as st
import requests
from streamlit_lottie import st_lottie
from Encryption import main as encrypt_main
from Decryption import main as decrypt_main

st.markdown(
        """
        <style>
            .st-emotion-cache-1y4p8pa {
                max-width: 70rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# take image as input from user 
st.write("Image to image encryption")
image = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
# run main function from the encryption file
if image:
    # st.image(image)
    encrypt_main(image)
    # display the encrypted image
    # st.image('encrypted_image_from_image.png')
    # st.write('Image encrypted successfully')
    button_clicked = st.button("Show Encrypted Image")
    button_clicked1 = st.button("Show Encrypted Text")
    if button_clicked:
        st.image('encrypted_image_from_image.png')
        st.write('Image encrypted successfully')

    if button_clicked1:
        with open('encrypted_text.txt', 'r') as file:
            data = file.read()
            st.write(data)

st.write("Image to image decryption")


button_clicked = st.button("Decrypt Image")

# Check if the button is clicked
if button_clicked:
    # run main function from the decryption file
    decrypt_main('encrypted_text.txt')
    # display the decrypted image
    st.image('decrypted_image_from_image.png')
    st.write('Image decrypted successfully')

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            You can use this app to encrypt and decrypt images. 

            - Images are convert to encrypted images .
            - encrypted images are converted to encrypted text .
            - encrypted text is converted to decrypted text .
            - decrypted text is converted to decrypted images .

            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")



