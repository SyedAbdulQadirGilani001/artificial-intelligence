# import streamlit as st
# import seaborn as sns
# st.header('Hello World')
# st.text('Enjoy')
# st.header('Second Heading')
# df=sns.load_dataset('iris')
# st.write(df[['species','sepal_length','petal_length']].head())
# st.bar_chart(df['sepal_length'])
# st.line_chart(df['sepal_width'])
import streamlit as st
from streamlit_embedcode import github_gist
link='https://gist.github.com/SyedAbdulQadirGilani001/8e4fadebff5bfe33dd148d2551d75619'
st.write('Embed Code')
github_gist(link)