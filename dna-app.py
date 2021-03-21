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

    ***
    """
)

# Input text box
st.header("Enter DNA sequence")

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=200)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = "".join(sequence)

st.write(
    """
    ***
    """
)

## Prints the input DNA sequence
st.header("INPUT (DNA Query)")
sequence

## DNA nucleotide count
st.header("OUTPUT (DNA Nucleotide Count)")

### 1. Print dictionnary
st.subheader("1. Print dictionnary")


def dna_nucleotide_count(seq):
    return dict(
        [
            ("A", seq.count("A")),
            ("T", seq.count("T")),
            ("G", seq.count("G")),
            ("C", seq.count("C")),
        ]
    )


results = dna_nucleotide_count(sequence)
results

### 2. Print text
st.subheader("2. Print text")
st.write("There are " + str(results["A"]) + " adenosine (A)")
st.write("There are " + str(results["T"]) + " thymine (T)")
st.write("There are " + str(results["G"]) + " guanine (G)")
st.write("There are " + str(results["C"]) + " cytosine (C)")

### 3. Display Dataframe
st.subheader("3. Display Dataframe")
df = pd.DataFrame.from_dict(results, orient="index")
df = df.rename({0: "Count"}, axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns={"index": "Nucleotide"})
st.write(df)

### 4. Display Bar Chart with Altair
st.subheader("4. Display Bar Chart with Altair")
p = alt.Chart(df).mark_bar().encode(x="Nucleotide", y="Count")
p = p.properties(width=alt.Step(80))
st.write(p)
