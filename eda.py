from distutils.command.upload import upload
import re
from turtle import up
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
st.markdown('''**EDA Data Analysis Web App**''')
with st.sidebar.header('Select Data'):
    uploaded_file = st.sidebar.file_uploader('Upload a CSV file', type='csv')
    df=sns.load_dataset('tips')
    st.sidebar.markdown('[Example Data](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)')
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv=pd.read_csv(uploaded_file)
        return csv
    df=load_csv()
    pr=ProfileReport(df,explorative=True)
    st.header('**Data Profile**')
    st.write(df.shape)
    st.write('___')
    st.write(df.info())
    st_profile_report(pr)
else:
    st.info('No data uploaded')
    if st.button('Upload Data'):
        @st.cache
        def load_data():
            df=pd.DataFrame(np.random.randn(10,5),columns=['A','B','C','D','E'])
            return df
        df=load_data()
        pr=ProfileReport(df,explorative=True)