from distutils.command.upload import upload
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
st.markdown(""" #### EDA""")
with st.sidebar.header('Upload Data'):
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv", "txt"])
    df=sns.load_dataset('titanic')
    st.sidebar.markdown("[data](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)")
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv=pd.read_csv(uploaded_file)
        return csv
    df=load_csv()
    pr=ProfileReport(df,explorative=True)
    st.header('**INPUT DF**')
    st.write(df)
    st.write('---')
    st.write('**Pandas Profiling Report')
    st_profile_report(pr)
else:
    st.info('Waiting for input data')
    if st.button('Generate Profile Report'):
        @st.cache
        def load_data():
            a=pd.DataFrame(np.random.randn(100,5))
            return a
        df=load_data()
        pr=ProfileReport(df,explorative=True)
# st.success('Success message')
# st.color_picker('Pick a color')