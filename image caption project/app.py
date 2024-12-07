import streamlit as st 
import requests 
from PIL import Image 
from io import BytesIO

# streamlit UI for image upload 
st.title("Image Captioning with BLIP")
st.write("Upload an Image, and the model will generate a caption for it.")


uploaded_file = st.file_uploader("Choose an image...", type=['png' , 'jpg' , 'jpeg'])

if uploaded_file is not None:
    # Display the uploaded image 
    image = Image.open(uploaded_file)

    st.image(image, caption = 'Uploaded Image', use_container_width= True)

    # Button to generate caption 
    if st.button("generate"):
        with st.spinner('Generating Captions...'):
            # send image to fastapi backend 
            response = requests.post(
                "http://127.0.0.1:8000/generate-caption/",
                files={"file": uploaded_file.getvalue()}
            )
            caption_data = response.json()

            if "caption" in caption_data:
                st.write(f"Generated Caption: {caption_data['caption']}")
            else:
                st.error("Failed to generate caption. Please try again")

    


