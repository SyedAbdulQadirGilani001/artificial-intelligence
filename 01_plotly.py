from turtle import width
from matplotlib import animation
import streamlit as st
import plotly.express as px
import pandas as pd
st.title('Plotly & Streamlit')
df=px.data.gapminder()
st.write(df.head())
st.write(df.columns)
st.write(df.describe())
year_option=df['year'].unique().tolist()
year=st.selectbox('Select Year',year_option,0)
# df=df[df['year']==year]
fig=px.scatter(df,x='gdpPercap',
y='lifeExp',size='pop',color='continent',
hover_name='continent',log_x=True,size_max=55,
range_x=[100,100000000],range_y=[20,90],animation_frame='year',
animation_group='country')
fig.update_layout(width=800,height=400)
st.write(fig)