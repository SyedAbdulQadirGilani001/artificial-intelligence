from operator import irshift

from sklearn import datasets
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
st.write(""" # Random Forest Classifier""")
st.sidebar.header("Load Data")
def user_input_features():
    sepal_length=st.sidebar.slider("Sepal Length", 4.3, 7.9, 5.4)
    sepal_width=st.sidebar.slider("Sepal Width", 2.0, 4.4, 3.4)
    petal_length=st.sidebar.slider("Petal Length", 1.0, 6.9, 1.3)
    petal_width=st.sidebar.slider("Petal Width", 0.1, 2.5, 0.2)
    data={'sepal_length':sepal_length,
            'sepal_width':sepal_width,
            'petal_length':petal_length,
            'petal_width':petal_width}
    features=pd.DataFrame(data, index=[0])
    return features
df=user_input_features()
st.subheader('User Inputs')
st.write(df)
iris=datasets.load_iris()
x=iris.data
y=iris.target
rfc=RandomForestClassifier()
rfc.fit(x,y)
prediction=rfc.predict(df)
prediction_price=rfc.predict_proba(df)
st.subheader('Prediction')
st.write(iris.target_names[prediction])
st.subheader('Prediction Probability')
st.write(prediction_price)
st.subheader('Random Forest Classifier')
st.write(rfc)
st.subheader('Random Forest Classifier Score')
st.write(rfc.score(x,y))
st.subheader('Random Forest Classifier Feature Importance')
st.write(rfc.feature_importances_)
st.subheader('Random Forest Classifier Feature Importance')
st.subheader('Classes')
st.write(iris.target_names)