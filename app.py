import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
header=st.container()
data_sets=st.container()
features=st.container()
model_training=st.container()
with header:
    st.title('Titanic App')
    st.text('Titanic Data')
with data_sets:
    st.header('Titanic Destroyed')
    st.text('Titanic Dataset')
    df=sns.load_dataset('titanic')
    df=df.dropna()
    st.write(df.head())
    st.subheader('How many Mans?')
    st.bar_chart(df['sex'].value_counts())
    st.subheader('Class Difference')
    st.bar_chart(df['class'].value_counts())
    st.bar_chart(df['age'].sample())
with features:
    st.header('App Features')
    st.text('Titanic Features')
    st.markdown('**Features**')
with model_training:
    st.header('What Happened to Titanic Passengers')
    st.text('Model Training')
    input,display=st.columns(2)
    max_depth=input.slider('How many people are there',min_value=10,max_value=100,value=20,step=5)
n_estimators=input.selectbox('How many tree should be there in a RF?',options=[50,100,200,300,'No Limit'])
input.write(df.columns)
input_features=input.text_input('Which Feature to use')
model=RandomForestRegressor(max_depth=max_depth,n_estimators=n_estimators)
if n_estimators=='No Limit':
    model=RandomForestRegressor(max_depth=max_depth)
else:
    model=RandomForestRegressor(max_depth=max_depth,n_estimators=n_estimators)
x=df[[input_features]]
y=df[['fare']]
model.fit(x,y)
pred=model.predict(y)
display.subheader('Mean Absolute Error of the Model')
display.write(mean_absolute_error(y,pred))
display.subheader('Mean Squared Error of the Model')
display.write(mean_squared_error(y,pred))
display.subheader('R Squared Score of the Model')
display.write(r2_score)