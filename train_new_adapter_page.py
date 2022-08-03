import glob
import pandas as pd
import streamlit as st
from run_prediction import predict_scores

from packages.utils import ADAPTERS_PATH

"""
This page is for training a new adapter.

"""


def show_train_adapter_page():
    st.title("Train new adapter")

    st.subheader("Please upload you data as SMILES in csv or txt file")
    data_file = st.file_uploader("Upload data", type=["csv", "txt"])

    st.select_slider("Select the type of the task", ["Regression", "Classification"])
