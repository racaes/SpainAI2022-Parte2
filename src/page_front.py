import streamlit as st


def front():
    text = """
            # This is a test
            
            """
    st.write(text)

    image_huggingface_url = "https://avatars.githubusercontent.com/u/25720743?s=200"
    st.image(image_huggingface_url)

    text = "HuggingFace"
    url = "https://huggingface.co/"
    link = "[%s](%s)" % (text, url)
    st.write(link)
