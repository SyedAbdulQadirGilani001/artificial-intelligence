from email.mime import audio
import streamlit as st
from PIL import Image
st.write('# Media Files in Streamlit app')
image=Image.open('download.jfif')
st.image(image)
video=open('snow.mp4','rb')
st.video(video)
audio=open('snow.mp3','rb')
st.audio(audio)
# from pyexpat import model
# from sklearn.ensemble import RandomForestClassifier
# from explainerdashboard import ClassifierExplainer, ExplainerDashboard
# from explainerdashboard.datasets import titanic_survive,feature_descriptions
# x_train,y_train,x_test,y_test=titanic_survive()
# model=RandomForestClassifier().fit(x_train,y_train)
# explainer=ClassifierExplainer(model,x_test,y_test,cats=['Sex','Deck','Embarked'],discriptions=feature_descriptions,labels=['Not Survived','Survived'])
# ExplainerDashboard(explainer).run()