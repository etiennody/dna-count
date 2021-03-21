import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

# Page title
image = Image.open("dna-logo.jpg")

st.image(image, use_column_width=True)

st.write(
    """
    # DNA Nucleotide Count Web App

    This application counts the nucleotide composition of query DNA!

    """
)
