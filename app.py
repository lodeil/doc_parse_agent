#!/bin/sh tesseract --version && tesseract --list-langs


import os
import json
import io
import streamlit as st
import pytesseract
import PyPDF2
import openpyxl
from functions import *



# Config :
# To launch : streamlit run app.py
# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'D:\\softwares\\Tesseract-OCR\\tesseract.exe'

def image_to_text(file):

    contents = file.read()
    pil_image = Image.open(io.BytesIO(contents))
    # Simple image to string
    text_of_image = pytesseract.image_to_string(pil_image)

    return text_of_image

st.set_page_config(
    page_title="Documents to text",
    page_icon="🌠",
)
st.header("")
st.title("🌳 Parse your documents ")
st.header("")

with st.expander("ℹ️ - Information on this app", expanded=True):

    st.write(
        """     
-   The *Documents to text* is an easy-to-use interface for parsing a document
-   It build to be easy to use with nominal performance 
	    """
    )

    st.markdown("")

st.header("")
st.markdown("🌌 Select your files ")
st.header("")

with st.form(key="my_form"):

    c29, c30, c31 = st.columns([0.08, 6, 0.18])

    with c30:


        files = st.file_uploader(
            "",
            key="1",
            help="To activate 'wide mode', go to the hamburger menu > Settings > turn on 'wide mode'",
            accept_multiple_files=True
        )

        st.info(
                f"""
                    👆 Upload a file first. Here is a sample to try: [trees.csv](https://people.sc.fsu.edu/~jburkardt/data/csv/trees.csv)
                    """
            )

        submit_button = st.form_submit_button(label="🧾 Parse it all !")


if not submit_button:
    st.stop()

st.markdown("🌲 Your files as a text ")

text_of_files = files_to_text(files=files)

st.text(
    text_of_files
    )

st.markdown("🌼 The end 🌼")