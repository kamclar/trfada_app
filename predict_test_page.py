import glob
import pandas as pd
import streamlit as st
from make_plots import get_corr_plot
from run_prediction import predict_scores

from packages.utils import ADAPTERS_PATH

"""
This page is for computing docking score values for a testset
with precomputed values, so comparison of predicted and original 
values can be made.

"""

def show_predict_test_page():
    st.title("Predict the docking scores")

    st.subheader("Please upload you test dataset as SMILES, with columns with computed docking score values -  in csv or txt file")
    data_file = st.file_uploader("Upload data", type=["csv", "txt"])

    if data_file is not None:
            # To See details
            file_details = {"filename":data_file.name, 
                            "filetype":data_file.type,
                            "filesize":data_file.size}
            st.write(file_details)            
            df = pd.read_csv(data_file)
            st.dataframe(df.head())

    names =[n.replace(ADAPTERS_PATH, "") for n in glob.glob(ADAPTERS_PATH+"docking*")]
    ok = st.button("Predict the score values.")

    if ok:
        preds_df = predict_scores(names, df)        

        st.subheader("Predicted score values for each docking function type")
        st.dataframe(preds_df.head())

        preds_df.to_csv('trf-ada_predicted_testset_scores.csv', index=False)
        st.download_button('Download CSV', 'trf-ada_predicted_testset_scores.csv', 'text/csv')            
        fig = get_corr_plot(df,preds_df)
        st.pyplot(fig)

    


