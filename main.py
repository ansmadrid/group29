import streamlit as st

header = st.container()
dataset = st.container()

with header:
    st.title("Medical Image Analysis and Classification")
    st.text("Classification of DermaMnist and RetinaMnist datasets")

with dataset:
    st.subheader("The dataset are trained using Convolutional Neural Network (CNN) and Multi-Layer Perceptron (MLP)")
    st.selectbox("Select the dataset", ["DermaMnist", "RetinaMnist"])
    st.file_uploader("Upload image here", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
    st.button("Classify")